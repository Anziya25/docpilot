from app.services.document_loader import DocumentLoader

loader = DocumentLoader()

docs = loader.load_document("/home/aiml-12/Downloads/projects/rag/enterprise-rag-faiss-openai/uploads/anziya.docx")   # Change to your actual filename

print("=" * 80)
print("Total Documents:", len(docs))
print("=" * 80)

print(docs[0].page_content)