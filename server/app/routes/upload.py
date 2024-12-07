import os
import asyncio
from typing import List
from fastapi import APIRouter, UploadFile, HTTPException

from config import Config
from src.database import save_metadata_to_db

router = APIRouter()


@router.post("/upload/")
async def upload_file(files: List[UploadFile]):
    """
    Эндпоинт для загрузки архива документов.
    """
    files = await asyncio.gather(*[process_file(file) for file in files])
    files = [{"filename": filename, "content_type": content_type, "ext": ext, "status": status}
             for (filename, content_type, ext, status) in files]
    return {
        "message": "Files processed",
        "files": files
    }

async def process_file(file: UploadFile):
    filename = file.filename
    content_type = file.content_type
    ext = Config.ALLOWED_EXTENSIONS.get(file.content_type)
    filename = filename[::-1].replace(ext[::-1], '', 1)[::-1]

    if file.content_type not in Config.ALLOWED_EXTENSIONS.keys():
        return filename, content_type, ext, "400 Invalid document type"

    status = save_metadata_to_db(filename, content_type, ext, Config.DB_PATH)

    try:
        # Сохраняем загруженный файл
        os.makedirs(Config.FILES_FOLDER, exist_ok=True)
        file_path = os.path.join(Config.FILES_FOLDER, file.filename)
        with open(file_path, "wb") as f:
            f.write(await file.read())
    except:
        status = "500 Internal Server Error"

    return filename, content_type, ext, status
