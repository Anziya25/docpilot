from app.services.document_loader import DocumentLoader
from app.services.chunker import TextChunker

# Initialize
loader = DocumentLoader()
chunker = TextChunker()

# Load a PDF
documents = loader.load_document(
    "/home/aiml-12/Downloads/projects/rag/enterprise-rag-faiss-openai/documents/papers/attention.pdf"
)

print("=" * 60)
print(f"Original Documents : {len(documents)}")

# Split into chunks
chunks = chunker.split_documents(documents)

print(f"Total Chunks       : {len(chunks)}")
print("=" * 60)

# Show first chunk
print("First Chunk Metadata")
print(chunks[0].metadata)

print("=" * 60)

print("First Chunk Preview")
print(chunks[0].page_content[:800])

print("=" * 60)