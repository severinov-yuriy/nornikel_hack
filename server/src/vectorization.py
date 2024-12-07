from typing import List
from fastembed import TextEmbedding

class TextVectorizer:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        """
        Инициализация векторизатора текста с использованием FastEmbed.
        :param model_name: Имя модели для векторизации.
        """
        self.model = TextEmbedding(model_name="BAAI/bge-small-en-v1.5")

    def vectorize(self, texts: List[str]) -> List[List[float]]:
        """
        Векторизация списка текстов.
        :param texts: Список текстовых строк.
        :return: Список векторных представлений.
        """
        # Векторизация текстов
        return list(self.model.embed(texts))  # Преобразование в список для совместимости
