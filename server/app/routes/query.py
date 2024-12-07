from fastapi import APIRouter, HTTPException
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
        rag = RAGPipeline(
            vector_store_path=Config.VECTOR_STORE_PATH,
            db_path=Config.DB_PATH,
            vector_dim=Config.VECTOR_DIM
        )
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
        raise HTTPException(status_code=500, detail=f"Error processing query: {str(e)}") 
