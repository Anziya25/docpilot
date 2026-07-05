from app.services.document_loader import DocumentLoader

loader = DocumentLoader()

# Change the file path to test different document types
file_path = "/home/aiml-12/Downloads/projects/rag/enterprise-rag-faiss-openai/documents/papers/attention.pdf"

# file_path = "documents/papers/attention_is_all_you_need.pdf"
# file_path = "documents/books/sample.docx"

documents = loader.load_document(file_path)

print("=" * 60)
print("DOCUMENT LOADER TEST")
print("=" * 60)

print(f"Documents Loaded : {len(documents)}")

print("=" * 60)

print("Metadata")

print(documents[0].metadata)

print("=" * 60)

print("Content Preview")

print(documents[0].page_content[:1000])

print("=" * 60)