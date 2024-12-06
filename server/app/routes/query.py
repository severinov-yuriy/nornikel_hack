from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class QueryRequest(BaseModel):
    query: str
    api_type: str = None
    api_key: str = None
    api_url: str = None  # Для кастомных моделей
    model_name: str = "meta-llama/llama-3.1-70b-instruct:free"
    top_k: int = 1

@router.post("/query/")
async def handle_query(request: QueryRequest):
    """
    Эндпоинт для обработки запросов пользователя с использованием RAG.
    """
    response = {
        "query": request.query,
        "answer": "This is just a chill answer",
        "context_files": [
            "file 1",
            "file 2",
            "file 42",
            "file 34"
            ]
        }
    return response
