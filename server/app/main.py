import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import upload, query, files
from src.database import init_database
from config import Config
from src.weaviate_database import WeaviateClient

# Инициализация базы данных
os.makedirs(Config.DATA_FOLDER, exist_ok=True)
init_database(Config.DB_PATH)
weaviate_client = WeaviateClient(in_docker=True)

# Инициализация приложения
app = FastAPI(
    title="RAG Service",
    description="A Retrieval-Augmented Generation (RAG) Service for document indexing",
    version="1.0.0",
)

# Регистрация маршрутов
app.include_router(upload.router, tags=["Filesystem"])
app.include_router(query.router, tags=["Query"])
app.include_router(files.router, tags=["Filesystem"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Точка входа для проверки статуса
@app.get("/")
async def root():
    return {"message": "RAG Service is running"}
