import os
from typing import List
from src.text import (
    process_txt,
    process_doc,
    process_pdf,
    preprocess_text,
    split_into_chunks,
)

# from src.audio import process_audio
# from src.image import process_image
from src.database import save_text, save_chunk
from src.vectorization import TextVectorizer
from src.vector_store import VectorStore

EXTRACTORS = {
    "text/plain": process_txt,
    "application/msword": process_doc,
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document": process_doc,
    "application/pdf": process_pdf,
    # "audio/mpeg": process_audio,
    # "image/jpeg": process_image,
    # "image/png": process_image,
}


def process_files(files: List[dict], config):
    """
    Пайплайн обработки списка загруженных файлов.

    :param files: Список файлов.
    :param data_dir: Папка с данными.
    :param files_dir: Папка с файлами.
    :return: Список словарей с кусочками текста.
    """
    chunk_data = []
    for file in files:
        try:
            extract = EXTRACTORS.get(file.get("content_type"))
            filepath = os.path.join(
                config.FILES_FOLDER, file.get("filename"), file.get("ext")
            )
            text = extract(filepath)
            text = preprocess_text(text)
            save_text(file.get("file_id"), text, config.DB_PATH)
            chunks = split_into_chunks(text, config.CHUNK_SIZE, config.OVERLAP)
            for chunk in enumerate(chunks):
                chunk_id = save_chunk(chunk, file.get("file_id"), config.DB_PATH)
                chunk_data.append({"id": chunk_id, "chunk": chunk})
        except Exception as e:
            print(f"Error processing {file.get('file_id')}: {e}")
        vectorizer = TextVectorizer()
        idx = [chunk["id"] for chunk in chunks]
        texts = [chunk["chunk"] for chunk in chunks]
        vectors = vectorizer.vectorize(texts)

        # Инициализируем векторное хранилище и индексируем кусочки
        vector_store = VectorStore(config.VECTOR_DIM, config.VECTOR_STORE_PATH)
        vector_store.add_vectors(idx, vectors)
        vector_store.save_index()
