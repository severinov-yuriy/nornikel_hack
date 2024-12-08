import os
from typing import List
from src.text import (
    process_txt,
    process_doc,
    process_pdf,
    preprocess_text,
    split_into_chunks,
)

from src.audio import process_audio
from src.image import process_image
from src.database import save_text, save_chunk
from src.weaviate_database import get_weaviate_client
from tqdm.auto import tqdm
import asyncio
import httpx
from src.logger import logger

EXTRACTORS = {
    "text/plain": process_txt,
    "application/msword": process_doc,
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document": process_doc,
    "application/pdf": process_pdf,
    "audio/mpeg": process_audio,
    "image/jpeg": process_image,
    "image/png": process_image,
}

async def external_extract(files: list[dict], base_url: str) -> list[str]:
    filesopens = {
        'documents': (
            file['filename'],
            open(file['filepath'], 'rb'),
            'application/pdf'
        )
        for file in files
    }
    async with httpx.AsyncClient() as client:
        create_job_url = f"{base_url}/batch-conversion-jobs"
        response = await client.post(create_job_url, files=filesopens)
        response.raise_for_status()

        job_id = response.json().get("job_id")
        if not job_id:
            raise RuntimeError("Failed to create batch conversion job: Missing job_id in response.")

        get_job_status_url = f"{base_url}/batch-conversion-jobs/{job_id}"
        while True:
            status_response = await client.get(get_job_status_url)
            status_response.raise_for_status()

            job_status = status_response.json()
            if job_status.get("status") == "SUCCESS":
                return job_status
            elif job_status.get("status") == "FAILURE":
                raise RuntimeError(f"Batch conversion job failed: {job_status}")
            await asyncio.sleep(10)


async def external_extract_one_file(file: dict, base_url: str):
    filesopens = {
        'document': (
            file['filename'],
            open(file['filepath'], 'rb'),
            'application/pdf'
        )
    }
    try:
        async with httpx.AsyncClient() as client:
            create_job_url = f"{base_url}/conversion-jobs"
            response = await client.post(create_job_url, files=filesopens)
            response.raise_for_status()

            job_id = response.json().get("job_id")
            if not job_id:
                raise RuntimeError("Failed to create batch conversion job: Missing job_id in response.")

            get_job_status_url = f"{base_url}/conversion-jobs/{job_id}"
            while True:
                status_response = await client.get(get_job_status_url)
                status_response.raise_for_status()

                job_status = status_response.json()
                if job_status.get("status") == "SUCCESS":
                    return job_status
                elif job_status.get("status") == "FAILURE":
                    raise RuntimeError(f"Batch conversion job failed: {job_status}")
                await asyncio.sleep(10)
    finally:
        for _, file, _ in filesopens.values():
            file.close()

async def process_one_file(file: dict, config):
    job_result = await external_extract_one_file(file, os.getenv('DOCLING_SERVER'))
    text = job_result["result"]["markdown"]
    chunk_data = []
    try:
        text = preprocess_text(text)
        save_text(file.get("file_id"), text, config.DB_PATH)
        chunks = split_into_chunks(text, config.CHUNK_SIZE, config.OVERLAP)
        for chunk in chunks:
            chunk_id = save_chunk(chunk, file.get("file_id"), config.DB_PATH)
            chunk_data.append({"id": chunk_id, "chunk": chunk})
    except Exception as e:
        logger.error(f"Error processing {file.get('file_id')}: {e}")

    get_weaviate_client().add_documents([
        {
            "title" : file.get('filename', "Unknown"),
            "chunk_id" : id_and_chunk["id"],
            "content" : id_and_chunk["chunk"],
        }
        for id_and_chunk in chunk_data
    ])
    logger.info(f"Ready file {file.get('file_id')=} {file.get('filename')=}")

async def process_files(files: List[dict], config):
    asyncio.gather(*[process_one_file(file, config) for file in tqdm(files, desc="Processing files")])

def process_files_gold(files: List[dict], config):
    """
    Пайплайн обработки списка загруженных файлов.

    :param files: Список файлов.
    :param data_dir: Папка с данными.
    :param files_dir: Папка с файлами.
    :return: Список словарей с кусочками текста.
    """
    chunk_data = []
    for file in tqdm(files):
        try:
            extract = EXTRACTORS.get(file.get("content_type"))
            filepath = file['filepath']
            text = extract(filepath)
            text = preprocess_text(text)
            save_text(file.get("file_id"), text, config.DB_PATH)
            chunks = split_into_chunks(text, config.CHUNK_SIZE, config.OVERLAP)
            for chunk in chunks:
                chunk_id = save_chunk(chunk, file.get("file_id"), config.DB_PATH)
                chunk_data.append({"id": chunk_id, "chunk": chunk})
        except Exception as e:
            logger.error(f"Error processing {file.get('file_id')}: {e}")

        get_weaviate_client().add_documents([
            {
                "title" : file.get('filename', "Unknown"),
                "chunk_id" : id_and_chunk["id"],
                "content" : id_and_chunk["chunk"],
            }
            for id_and_chunk in chunk_data
        ])
        logger.info(f"Ready file {file.get('file_id')=} {file.get('filename')=}")
