from app.config.settings import *

print("=" * 50)
print("Configuration Test")
print("=" * 50)

print("OpenAI API Key      :", OPENAI_API_KEY)
print("LLM Model           :", LLM_MODEL)
print("Embedding Model     :", EMBEDDING_MODEL)
print("Chunk Size          :", CHUNK_SIZE)
print("Chunk Overlap       :", CHUNK_OVERLAP)
print("Upload Folder       :", UPLOAD_FOLDER)
print("Vector Store Folder :", VECTOR_STORE_PATH)

print("=" * 50)
print("Configuration Loaded Successfully!")