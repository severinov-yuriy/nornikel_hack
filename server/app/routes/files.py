import os
from typing import Optional
from fastapi import APIRouter
from fastapi.responses import FileResponse
from config import Config
from src.database import get_filename_by_id, get_files_list, delete_by_id

router = APIRouter()


@router.get("/files/")
def get_files(id: Optional[int] = None):
    """
    Эндпоинт для скачивания файла с бэка.
    """
    if id:
        filename, ext, content_type = get_filename_by_id(id, Config.DB_PATH)
        file_path = os.path.join(Config.FILES_FOLDER, f"{filename}{ext}")
        return FileResponse(path=file_path, filename=f"{filename}{ext}", media_type=content_type)
    return get_files_list(Config.DB_PATH)

@router.delete("/files/{id}")
def delete_file(id: int):
    """
    Эндпоинт для скачивания файла с бэка.
    """
    filename, ext, _ = get_filename_by_id(id, Config.DB_PATH)
    os.remove(f'{Config.FILES_FOLDER}/{filename}{ext}')
    return delete_by_id(id, Config.DB_PATH)
