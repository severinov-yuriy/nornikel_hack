from src.weaviate_database import WeaviateClient
import sys


def test_weaviate_client():
    client = WeaviateClient(in_docker=False)
    assert client.is_ready()

    try:
        client.delete_classic_schema()
    except Exception as e:
        print(f"Warning deleting schema: {e}", file=sys.stderr)

    client.set_classic_schema()
    client.add_sample_documents()

    assert client.is_ready()

    response = (
        client.client.query.get("Wine", ["name", "review"])
        .with_near_text({"concepts": ["great for seafood"]})
        .do()
    )
    print(response, file=sys.stderr)
    assert "errors" in response

    response = (
        client.client.query.get("Document", ["title", "content"])
        .with_near_text({"concepts": ["about AI"]})
        .do()
    )
    print(response, file=sys.stderr)

    assert response["data"]["Get"]["Document"][0]["title"] == "AI Revolution"
    client.close()
