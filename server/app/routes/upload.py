import os
import asyncio
from typing import List
from fastapi import APIRouter, UploadFile, BackgroundTasks
from PyPDF2 import PdfReader, PdfWriter
from config import Config
from src.database import save_metadata_to_db
from src.processing import process_files, process_files_gold
import itertools

router = APIRouter()


@router.post("/upload/")
async def upload_file(files: List[UploadFile], background_tasks: BackgroundTasks):
    """
    Эндпоинт для загрузки архива документов.
    """

    files = await asyncio.gather(*[process_file(file) for file in files])
    files = [{"file_id": file_id, "filename": filename, "content_type": content_type, "ext": ext, "status": status, "filepath": filepath}
             for (file_id, filename, content_type, ext, status, filepath) in itertools.chain.from_iterable(files)]

    background_tasks.add_task(process_files_gold, files, Config)

    return {
        "message": "Files saved, it will appear after processing",
        "files": files
    }

async def process_file(file: UploadFile) -> list:
    filename = file.filename
    content_type = file.content_type
    if content_type not in Config.ALLOWED_EXTENSIONS.keys():
        return "None", filename, content_type, "400 Invalid document type"
    ext = Config.ALLOWED_EXTENSIONS.get(file.content_type)
    filename = filename.removesuffix(ext)
    os.makedirs(Config.FILES_FOLDER, exist_ok=True)
    os.makedirs(Config.FILES_FOLDER, exist_ok=True)
    file_path = os.path.join(Config.FILES_FOLDER, file.filename)
    with open(file_path, "wb") as f:
        f.write(await file.read())
    file_id, status = save_metadata_to_db(filename, content_type, ext, Config.DB_PATH)
    ret = [[file_id, filename, content_type, ext, status, file_path]]

    if ext == ".pdf":
        ret = []
        output_file_paths = split_pdf(filename, file_path, Config.FILES_FOLDER)
        for output_file_path in output_file_paths:
            fi, st = save_metadata_to_db(os.path.basename(output_file_path), content_type, ext, Config.DB_PATH)
            ret.append([fi, os.path.basename(output_file_path), content_type, ext, st, output_file_path])

    return ret

def split_pdf(filename, input_pdf_path, output_dir):
    reader = PdfReader(input_pdf_path)
    total_pages = len(reader.pages)
    output_file_paths = []
    for i in range(total_pages):
        writer = PdfWriter()
        writer.add_page(reader.pages[0])
        writer.add_page(reader.pages[i])
        output_file_path = f"{output_dir}/{filename}_page_{i + 1}.pdf"
        with open(output_file_path, "wb") as output_file:
            writer.write(output_file)
        print(f"Page {i + 1} saved to {output_file_path}")
        output_file_paths.append(output_file_path)
    return output_file_paths
