from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

@router.post("/upload/")
async def handle_query(request):
    """
    Эндпоинт для обработки запросов пользователя с использованием RAG.
    """
    return f'{request=} received'