import os
from dotenv import load_dotenv

load_dotenv()


# Настройки приложения
class Config:

    # Настройки хранения данных
    DATA_FOLDER = "data"
    FILES_FOLDER = os.path.join(DATA_FOLDER, "files")
    PART_FILES_FOLDER = os.path.join(DATA_FOLDER, "part_files")
    DB_PATH = os.path.join(DATA_FOLDER, "database.db")
    VECTOR_STORE_PATH = os.path.join(DATA_FOLDER, "vector_store.index")
    ALLOWED_EXTENSIONS = {
        "text/plain": ".txt",
        "application/msword": ".doc",
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document": ".docx",
        "application/pdf": ".pdf",
        "audio/mpeg": ".mp3",
        "image/jpeg": ".jpeg",
        "image/png": ".png"
    }


    # Настройки обработки текста
    CHUNK_SIZE = 5120
    OVERLAP = 50

    # Настройки векторизации
    VECTOR_DIM = 384
    VECTORISER_NAME = "all-MiniLM-L6-v2"

    # Настройки языковой модели
    MODEL_NAME = "meta-llama/llama-3.1-70b-instruct:free"
    API_KEY = os.environ.get("API_KEY")
    API_TYPE = "openrouter"
    API_URL = None
    TOP_K = 20
