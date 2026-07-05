from pathlib import Path
from app.services.document_loader import DocumentLoader

loader = DocumentLoader()

pdfs = list(Path("uploads").glob("*.pdf"))

print(f"Found {len(pdfs)} PDFs\n")

for pdf in pdfs:
    docs = loader.load_pdf(str(pdf))
    print(pdf.name)
    print("Pages loaded:", len(docs))
    print("-" * 40)