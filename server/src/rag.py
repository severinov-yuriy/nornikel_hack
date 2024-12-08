from typing import List, Dict
from src.database import fetch_chunks_by_ids
from src.weaviate_database import get_weaviate_client

class RAGPipeline:
    def __init__(self, db_path: str):
        """
        Инициализация RAG-пайплайна.

        :param db_path: Путь к SQLite базе данных.
        :param vector_dim: Размерность векторов.
        :param model_name: Имя модели SentenceTransformers для векторизации.
        """
        self.db_path = db_path

    def retrieve_context(self, query: str, top_k: int = 10) -> List[Dict[str, str]]:
        """
        Извлечение релевантного контекста на основе пользовательского запроса.

        :param query: Запрос пользователя.
        :param top_k: Количество релевантных текстов для извлечения.
        :return: Список текстовых кусочков с метаданными.
        """
        response = (
            get_weaviate_client().client.query.get("Document", ["title", "content"])
            .with_limit(top_k)
            .with_near_text({"concepts": [query]})
            .do()
        )
        # Извлечение метаданных из базы данных
        chunk_ids = [x["chunk_id"] for x in response["data"]["Get"]["Document"]]  # Используем пользовательские идентификаторы
        print(chunk_ids)
        context_chunks = fetch_chunks_by_ids(chunk_ids, self.db_path)

        return context_chunks

    def generate_prompt(self, query: str, context_chunks: List[Dict[str, str]]) -> str:
        """
        Формирование промта для языковой модели.

        :param query: Запрос пользователя.
        :param context_chunks: Список текстовых кусочков для контекста.
        :return: Готовый промт.
        """
        context_texts = "\n\n".join([f"[{chunk['name']}]: {chunk['chunk_text']}" for chunk in context_chunks])
        prompt = f"""
            Ты аналитик. Твоя задача — предоставить четкий, обоснованный и краткий анализ ситуации.
            Используй данные и логику для поддержки своих выводов. Избегай лишних деталей и философствования.
            Если пользователь задал вопрос, ответ на него, используя данные, приведенные в поле Контекст ниже.
            Если пользователь не задал вопрос, сделай краткое саммари из поля Контекст ниже
            Контекст:
            {context_texts}
            Запрос пользователя: {query}
            Твой ответ:
            """
        return prompt

    def get_response(self, query: str, api_client, top_k: int, **kwargs) -> Dict[str, str]:
        """
        Получение ответа от языковой модели на основе RAG.

        :param query: Запрос пользователя.
        :param api_client: Клиент для взаимодействия с API модели (объект, реализующий метод `generate`).
        :param top_k: Количество релевантных текстов для извлечения.
        :param kwargs: Дополнительные параметры для метода `generate`.
        :return: Ответ и информация о контексте.
        """
        # Извлечение контекста
        context_chunks = self.retrieve_context(query, top_k)
        # Формирование промта
        prompt = self.generate_prompt(query, context_chunks)

        # Получение ответа от модели
        answer = api_client.generate(prompt, **kwargs)

        files = set(context_chunks)

        return {
            "query": query,
            "answer": answer,
            "files": files
            }