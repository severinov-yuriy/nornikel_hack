import os
from fastapi import APIRouter, UploadFile, HTTPException

router = APIRouter()

# Путь для сохранения временных файлов
TEMP_FOLDER = "data/uploads"
DB_PATH = "data/chunks.db"
VECTOR_STORE_PATH = "data/vector_store.index"
VECTOR_DIM = 384


@router.post("/upload/")
async def upload_archive(file: UploadFile):
    """
    Эндпоинт для загрузки архива документов.
    """
    # Создаем временную папку, если она не существует
    os.makedirs(TEMP_FOLDER, exist_ok=True)

    # Сохраняем загруженный файл
    archive_path = os.path.join(TEMP_FOLDER, file.filename)
    with open(archive_path, "wb") as f:
        f.write(await file.read())

    return {"message": "Archive processed successfully"}