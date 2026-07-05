"""
Test the complete indexing pipeline.
"""

from app.services.document_loader import DocumentLoader
from app.services.chunker import TextChunker
from app.services.embedder import EmbeddingService
from app.services.vector_store import VectorStoreService


def main():

    print("=" * 60)
    print("RESEARCH PAPER RAG - INDEXING PIPELINE")
    print("=" * 60)

    # Initialize services
    loader = DocumentLoader()
    chunker = TextChunker()
    embedder = EmbeddingService()
    vector_store = VectorStoreService()

    # Load PDF
    documents = loader.load_document(
        "documents/papers/attention.pdf"
    )

    print(f"Documents Loaded : {len(documents)}")

    # Chunk documents
    chunks = chunker.split_documents(documents)

    print(f"Chunks Created   : {len(chunks)}")

    # Create FAISS vector store
    print("\nCreating vector store...")

    db = vector_store.create_vector_store(
        chunks,
        embedder.get_embedding_model()
    )

    print("Vector store created successfully!")

    # Save index
    vector_store.save_vector_store(db)

    print("Vector store saved successfully!")

    print("=" * 60)
    print("INDEXING COMPLETED")
    print("=" * 60)


if __name__ == "__main__":
    main()