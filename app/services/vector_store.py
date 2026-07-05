"""
FAISS Vector Store Service

Creates, saves, loads and searches
the vector database.
"""

from pathlib import Path

from langchain_community.vectorstores import FAISS

from app.config.settings import VECTOR_STORE_PATH


class VectorStoreService:
    """
    Handles FAISS vector database operations.
    """

    def __init__(self):

        self.index_path = Path(VECTOR_STORE_PATH)

        # Create folder if it doesn't exist
        self.index_path.mkdir(parents=True, exist_ok=True)

    def create_vector_store(
        self,
        documents,
        embedding_model,
    ):
        """
        Create a FAISS index from documents.
        """

        vector_store = FAISS.from_documents(
            documents,
            embedding_model,
        )

        return vector_store

    def save_vector_store(
        self,
        vector_store,
    ):
        """
        Save the FAISS index.
        """

        vector_store.save_local(
            str(self.index_path)
        )

    def load_vector_store(
        self,
        embedding_model,
    ):
        """
        Load an existing FAISS index.
        """

        if not (self.index_path / "index.faiss").exists():
            raise FileNotFoundError(
                "Vector store not found. Please build the index first."
            )

        return FAISS.load_local(
            str(self.index_path),
            embedding_model,
            allow_dangerous_deserialization=True,
        )