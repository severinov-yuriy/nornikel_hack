from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from config import Config

router = APIRouter()


class QueryRequest(BaseModel):
    query: str


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
