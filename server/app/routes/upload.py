import os
import asyncio
from typing import List
from fastapi import APIRouter, UploadFile, BackgroundTasks

from config import Config
from src.database import save_metadata_to_db
from src.processing import process_files

router = APIRouter()


@router.post("/upload/")
async def upload_file(files: List[UploadFile], background_tasks: BackgroundTasks):
    """
    Эндпоинт для загрузки архива документов.
    """

    files = await asyncio.gather(*[process_file(file) for file in files])
    files = [{"file_id": file_id, "filename": filename, "content_type": content_type, "ext": ext, "status": status}
             for (file_id, filename, content_type, ext, status) in files]

    background_tasks.add_task(process_files, files, Config)

    return {
        "message": "Files saved, it will appear after processing",
        "files": files
    }

async def process_file(file: UploadFile):
    filename = file.filename
    content_type = file.content_type
    if file.content_type not in Config.ALLOWED_EXTENSIONS.keys():
        return "None", filename, content_type, "400 Invalid document type"
    ext = Config.ALLOWED_EXTENSIONS.get(file.content_type)
    file_id, status = save_metadata_to_db(filename, content_type, ext, Config.DB_PATH)
    try:
        os.makedirs(Config.FILES_FOLDER, exist_ok=True)
        file_path = os.path.join(Config.FILES_FOLDER, file.filename+ext)
        with open(file_path, "wb") as f:
            f.write(await file.read())
    except Exception as _:
        status = "500 Internal Server Error"
    return file_id, filename, content_type, ext, status
