import weaviate
import os
import sys

weaviate_client = None

class WeaviateClient:
    client: weaviate.Client

    def __init__(self, in_docker: bool):
        self.client = weaviate.Client(
            url="http://localhost:8080" if not in_docker else os.getenv("WEAVIATE_URL", "http://localhost:8080"),
        )

    def close(self):
        pass

    def __del__(self):
        self.close()

    def is_ready(self) -> bool:
        return self.client.is_ready()

    def set_classic_schema(self):
        assert self.is_ready()

        schema = {
            "classes": [
                {
                    "class": "Document",
                    "description": "A class to store documents",
                    "vectorizer": "text2vec-transformers",  # Use the local vectorizer
                    "properties": [
                        {
                            "name": "title",
                            "description": "The title of the document",
                            "dataType": ["text"],
                        },
                        {
                            "name": "chunk_id",
                            "description": "Chunk id",
                            "dataType": ["int"],
                        },
                        {
                            "name": "content",
                            "description": "The main content of the document",
                            "dataType": ["text"],
                        },
                    ],
                }
            ]
        }
        self.client.schema.create(schema)

    def delete_classic_schema(self):
        assert self.is_ready()
        self.client.schema.delete_class("Document")

    def add_documents(self, documents: list[dict[str, str]]) -> None:
        for doc in documents:
            self.client.data_object.create(data_object=doc, class_name="Document")

    def add_sample_documents(self) -> None:
        documents = [
            {
                "title": "AI Revolution",
                "chunk_id": 1,
                "content": "Artificial intelligence is transforming the world.",
            },
            {
                "title": "Climate Change Effects",
                "chunk_id": 1,
                "content": "Climate change has significant environmental impacts.",
            },
        ]
        for doc in documents:
            self.client.data_object.create(data_object=doc, class_name="Document")

def get_weaviate_client() -> WeaviateClient:
    global weaviate_client
    if weaviate_client is None:
        weaviate_client = WeaviateClient(in_docker=True)
        try:
            weaviate_client.delete_classic_schema()
            weaviate_client.set_classic_schema()
        except Exception as e:
            print(f"Warning setting up schema: {e}", file=sys.stderr)
    return weaviate_client