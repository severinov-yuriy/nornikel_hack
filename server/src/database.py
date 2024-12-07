import sqlite3

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
        chunk_id INTEGER PRIMARY KEY,
        chunk_text TEXT,
        file_id INTEGER
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS files_texts (    
        file_id INTEGER PRIMARY KEY,
        file_text TEXT,
        file_structure TEXT
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
        conn.close()
        return "200 File saved"

    except Exception as e:
        return f'503 DB error: {e}'

def get_filename_by_id(file_id: int, db_path: str):
    """
    Получение названия файла по его file_id.

    :return: Список названий файлов и их аттрибутов.
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    query = f"SELECT filename, ext FROM files WHERE file_id == {file_id}"
    cursor.execute(query)
    row = cursor.fetchall()
    conn.close()

    return row[0][0], row[0][1]

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