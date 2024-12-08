from fastapi import APIRouter
from pydantic import BaseModel
from config import Config
from src.rag import RAGPipeline
from src.api_clients import OpenRouterAPIClient

router = APIRouter()


class QueryRequest(BaseModel):
    query: str


@router.post("/query/")
async def handle_query(request: QueryRequest):
    """
    Эндпоинт для обработки запросов пользователя с использованием RAG.
    """
    try:
        # Инициализируем RAG-пайплайн
        rag = RAGPipeline(db_path=Config.DB_PATH)
        api_client = OpenRouterAPIClient(api_key=Config.API_KEY)

        # Обрабатываем запрос
        response = rag.get_response(
            query=request.query,
            api_client=api_client,
            top_k=Config.TOP_K,
            model=Config.MODEL_NAME
        )
        return response

    except Exception as e:
        raise e