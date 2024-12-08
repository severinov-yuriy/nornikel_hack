import sqlite3
from typing import List, Dict

# Создаем таблицу в SQLite для хранения метаданных
def init_database(db_path: str) -> None:
    """
    Инициализация базы данных: создание таблицы для хранения кусочков текста.

    :param db_path: Путь к файлу базы данных.
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS files (
        file_id INTEGER PRIMARY KEY AUTOINCREMENT,
        filename TEXT,
        content_type TEXT,
        ext TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS text_chunks (
        chunk_id INTEGER PRIMARY KEY AUTOINCREMENT,
        chunk_text TEXT,
        file_id INTEGER
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS files_texts (
        file_id INTEGER PRIMARY KEY,
        file_text TEXT
    )
    """)

    conn.commit()
    conn.close()

def save_metadata_to_db(filename: str, content_type: str, ext: str, db_path: str) -> None:
    """
    Сохранение метаданных файла в базу данных.

    :param filename: Название файла.
    :param content_type: Содержимое файла.
    :param ext: Расширение файла.
    :param db_path: Путь к файлу базы данных.
    """
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT OR IGNORE INTO files (filename, content_type, ext)
            VALUES (?, ?, ?)
            """,
            (filename, content_type, ext)
            )
        conn.commit()
        file_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return file_id, "200 File saved"

    except Exception as e:
        return "None", f'503 DB error: {e}'

def get_filename_by_id(file_id: int, db_path: str):
    """
    Получение названия файла по его file_id.

    :return: Список названий файлов и их аттрибутов.
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    query = f"SELECT filename, ext, content_type FROM files WHERE file_id == {file_id}"
    cursor.execute(query)
    row = cursor.fetchall()
    conn.close()

    return row[0][0], row[0][1], row[0][2]

def get_files_list(db_path: str):
    """
    Получение списка файлов из файловой системы.

    :return: Список названий файлов и их аттрибутов.
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    query = "SELECT file_id, filename, ext FROM files"
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()

    files = [{"id": row[0], "name": row[1], "ext": row[2]} for row in rows]

    return {"files": files, "total": len(files)}

def delete_by_id(file_id: int, db_path: str):
    """
    Получение названия файла по его file_id.

    :return: Список названий файлов и их аттрибутов.
    """
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        query = f"DELETE FROM files WHERE file_id = {file_id}"
        cursor.execute(query)
        conn.commit()
        conn.close()

        return "200 File deleted"

    except Exception as e:
        return f'503 DB error: {e}'

def save_text(file_id: str, text: str, db_path: str):
    """
    Сохранение текста файла в базу данных.

    :param file_id: ID файла.
    :param text: Текст из файла.
    :param db_path: Путь к файлу базы данных.
    """
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT OR IGNORE INTO files_texts (file_id, text)
            VALUES (?, ?)
            """,
            (file_id, text)
            )
        conn.commit()
        conn.close()
        return "200 File saved"
    except Exception as e:
        return f'503 DB error: {e}'


def save_chunk(chunk: str, file_id: str, db_path: str):
    """
    Сохранение текста файла в базу данных.

    :param chunk: Текст чанка.
    :param file_id: ID файла чанка.
    :param db_path: Путь к файлу базы данных.
    """
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT OR IGNORE INTO text_chunks (chunk_text, file_id)
            VALUES (?, ?)
            """,
            (chunk, file_id)
            )
        chunk_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return chunk_id
    except Exception as e:
        raise Exception(e)


def fetch_chunks_by_ids(ids: List[str], db_path: str = "data/chunks.db") -> List[Dict[str, str]]:
    """
    Извлечение кусочков текста по их идентификаторам.

    :param ids: Список идентификаторов чанков.
    :param db_path: Путь к файлу базы данных.
    :return: Список словарей с кусочками текста.
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    query = f"SELECT tc.chunk_id, f.filename, f.ext, tc.chunk_text FROM text_chunks tc LEFT JOIN files f ON tc.file_id==f.file_id WHERE tc.chunk_id IN ({','.join(['?'] * len(ids))})"
    cursor.execute(query, ids)
    rows = cursor.fetchall()
    
    print(rows)

    conn.close()

    return [{"id": row[0], "name": row[1], 'ext': row[2], "chunk_text": row[3]} for row in rows]
