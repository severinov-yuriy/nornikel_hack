import os
from fastapi import APIRouter
from fastapi.responses import FileResponse
from config import Config
from src.database import get_filename_by_id, get_files_list, delete_by_id

router = APIRouter()


@router.get("/files/")
def get_files(id: str = None):
    """
    Эндпоинт для скачивания файла с бэка.
    """
    if id:
        filename, ext = get_filename_by_id(id, Config.DB_PATH)
        print(f'{Config.FILES_FOLDER}/{filename}{ext}')
        return FileResponse(path=f'{Config.FILES_FOLDER}/{filename}{ext}', filename='filename')
    return get_files_list(Config.DB_PATH)

@router.delete("/files/")
def delete_file(id: str):
    """
    Эндпоинт для скачивания файла с бэка.
    """
    filename, ext = get_filename_by_id(id, Config.DB_PATH)
    os.remove(f'{Config.FILES_FOLDER}/{filename}{ext}')
    return delete_by_id(id, Config.DB_PATH)
