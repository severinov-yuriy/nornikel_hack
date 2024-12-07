import faiss
import numpy as np
from typing import List, Tuple


class VectorStore:
    def __init__(self, vector_dim: int, index_path: str = "data/vector_store.index"):
        """
        Инициализация векторного хранилища.
        :param vector_dim: Размерность векторов.
        :param index_path: Путь к файлу векторного индекса.
        """
        self.vector_dim = vector_dim
        self.index_path = index_path

        # Используем IndexIDMap для сохранения пользовательских идентификаторов
        self.index = faiss.IndexIDMap(faiss.IndexFlatL2(vector_dim))

    def add_vectors(self, ids: List[int], vectors: List[List[float]]) -> None:
        """
        Добавление векторов в хранилище.
        :param ids: Список идентификаторов.
        :param vectors: Список векторных представлений.
        """
        if len(ids) != len(vectors):
            raise ValueError(
                "Количество идентификаторов должно совпадать с количеством векторов."
            )

        vectors_np = np.array(vectors, dtype="float32")
        ids_np = np.array(ids, dtype="int64")  # FAISS требует идентификаторы в int64
        self.index.add_with_ids(vectors_np, ids_np)

    def search(
        self, query_vector: List[float], top_k: int = 10
    ) -> List[Tuple[int, float]]:
        """
        Поиск ближайших соседей по вектору.
        :param query_vector: Вектор запроса.
        :param top_k: Количество ближайших соседей.
        :return: Список идентификаторов и расстояний для ближайших соседей.
        """
        query_np = np.array([query_vector], dtype="float32")
        distances, indices = self.index.search(query_np, top_k)

        # Если в индексе нет данных, FAISS вернёт -1 как идентификатор
        return [
            (int(idx), float(dist))
            for idx, dist in zip(indices[0], distances[0])
            if idx != -1
        ]

    def save_index(self) -> None:
        """
        Сохранение индекса на диск.
        """
        faiss.write_index(self.index, self.index_path)

    def load_index(self) -> None:
        """
        Загрузка индекса с диска.
        """
        self.index = faiss.read_index(self.index_path)
        # Оборачиваем загруженный индекс в IndexIDMap для поддержки идентификаторов
        self.index = faiss.IndexIDMap(self.index)

    def get_vector_count(self) -> int:
        """
        Возвращает количество векторов в индексе.
        """
        return self.index.ntotal
