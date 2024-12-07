from typing import List
from fastembed import FastEmbed

class TextVectorizer:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        """
        Инициализация векторизатора текста с использованием FastEmbed.
        :param model_name: Имя модели для векторизации.
        """
        self.model = FastEmbed(model_name=model_name)

    def vectorize(self, texts: List[str]) -> List[List[float]]:
        """
        Векторизация списка текстов.
        :param texts: Список текстовых строк.
        :return: Список векторных представлений.
        """
        # Векторизация текстов
        embeddings = self.model.embed(texts)
        return embeddings.tolist()  # Преобразование в список для совместимости
