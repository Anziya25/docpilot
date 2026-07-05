"""
Retriever Service

Searches the FAISS vector database.
"""

from app.services.embedder import EmbeddingService
from app.services.vector_store import VectorStoreService


class RetrieverService:
    """
    Retrieves relevant chunks from FAISS.
    """

    def __init__(self):

        self.embedder = EmbeddingService()

        self.vector_store = VectorStoreService()

        self.db = self.vector_store.load_vector_store(
            self.embedder.get_embedding_model()
        )

    def search(
        self,
        query: str,
        k: int = 10,
    ):
        """
        Retrieve top-k similar chunks.
        """

        results = self.db.similarity_search_with_score(
            query,
            k=k,
        )

        print("\n" + "=" * 80)
        print("RETRIEVED CHUNKS")
        print("=" * 80)

        for i, (doc, score) in enumerate(results):

            print(f"\nResult {i+1}")
            print(f"Score : {score}")
            print(f"Metadata : {doc.metadata}")

            print("-" * 60)

            print(doc.page_content[:500])

            print("=" * 80)

        return results