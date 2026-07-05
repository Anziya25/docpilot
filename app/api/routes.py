from pathlib import Path
import shutil

from fastapi import APIRouter, File, UploadFile, HTTPException

from app.config.settings import UPLOAD_FOLDER

from app.services.document_loader import DocumentLoader
from app.services.chunker import TextChunker
from app.services.embedder import EmbeddingService
from app.services.vector_store import VectorStoreService

from app.core.rag import RAGPipeline

from app.models.chat_models import (
    ChatRequest,
    ChatResponse,
)

router = APIRouter()


# =====================================================
# Home
# =====================================================

@router.get("/")
def home():

    return {
        "message": "Enterprise Document Intelligence API"
    }


# =====================================================
# Health Check
# =====================================================

@router.get("/health")
def health():

    return {
        "status": "healthy"
    }


# =====================================================
# Upload Document
# =====================================================

@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):

    allowed_extensions = [".pdf", ".txt", ".docx"]

    extension = Path(file.filename).suffix.lower()

    if extension not in allowed_extensions:
        raise HTTPException(
            status_code=400,
            detail="Only PDF, TXT and DOCX files are allowed."
        )

    upload_dir = Path(UPLOAD_FOLDER)
    upload_dir.mkdir(parents=True, exist_ok=True)

    destination = upload_dir / file.filename

    with open(destination, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "message": "Upload successful",
        "filename": file.filename
    }


# =====================================================
# Build FAISS Vector Store
# =====================================================

@router.post("/index")
def build_index():

    upload_dir = Path(UPLOAD_FOLDER)

    all_files = []

    all_files.extend(upload_dir.glob("*.pdf"))
    all_files.extend(upload_dir.glob("*.txt"))
    all_files.extend(upload_dir.glob("*.docx"))

    if len(all_files) == 0:
        raise HTTPException(
            status_code=400,
            detail="No supported documents found in uploads folder."
        )

    loader = DocumentLoader()
    chunker = TextChunker()
    embedder = EmbeddingService()
    vector_store = VectorStoreService()

    all_documents = []

    # Load every document automatically
    for file in all_files:

        documents = loader.load_document(str(file))

        all_documents.extend(documents)

    # Split into chunks
    chunks = chunker.split_documents(all_documents)

    # Create FAISS database
    db = vector_store.create_vector_store(
        chunks,
        embedder.get_embedding_model()
    )

    # Save FAISS database
    vector_store.save_vector_store(db)

    return {
        "message": "Vector Store Created Successfully!",
        "uploaded_files": len(all_files),
        "documents_loaded": len(all_documents),
        "chunks_created": len(chunks)
    }


# =====================================================
# Chat with RAG
# =====================================================

@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    # Create a fresh RAG pipeline every request
    rag = RAGPipeline()

    result = rag.ask(request.question)

    return ChatResponse(
        answer=result["answer"],
        sources=result["sources"]
    )
