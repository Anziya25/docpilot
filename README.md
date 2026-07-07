<p align="center">
  <img src="screenshots/Workflow.png" alt="DocPilot Banner" width="100%">
</p>

# DocPilot

**AI-Powered Document Intelligence using Retrieval-Augmented Generation (RAG)**

DocPilot is a Retrieval-Augmented Generation (RAG) application that enables users to upload PDF, DOCX, and TXT documents and interact with them using natural language. The application indexes uploaded documents into a FAISS vector database and retrieves the most relevant context to generate accurate, context-aware responses using OpenAI Large Language Models (LLMs).

---

## Features

- Upload PDF, DOCX, and TXT documents
- Semantic document retrieval using FAISS
- AI-powered question answering
- Multi-document support
- Source-aware responses
- FastAPI backend
- React + TypeScript frontend
- Modular project architecture

---

# Workflow

<p align="center">
  <img src="screenshots/workflow.png" alt="DocPilot Workflow" width="100%">
</p>

---

# Application Preview

Application screenshots are available in the **`screenshots/`** directory.

---

# Requirements

Before running the project, install:

- Python 3.10+
- Node.js 18+
- npm
- Git

---

# Core Packages

Backend

- FastAPI
- LangChain
- OpenAI
- FAISS
- Sentence Transformers

Frontend

- React
- TypeScript
- Vite
- Tailwind CSS

Install all required dependencies using:

```bash
pip install -r requirements.txt
```

---

# Installation

Clone the repository.

```bash
git clone https://github.com/Anziya25/docpilot.git

cd enterprise-rag-faiss-openai
```

Create a virtual environment.

```bash
python3 -m venv .venv
```

Activate it.

### Linux / macOS

```bash
source .venv/bin/activate
```

### Windows

```cmd
.venv\Scripts\activate
```

Install backend dependencies.

```bash
pip install -r requirements.txt
```

Create a `.env` file.

```text
OPENAI_API_KEY=your_openai_api_key
```

Start the backend.

```bash
python app/main.py
```

---

# Frontend

```bash
cd frontend

npm install

npm run dev
```

---

# Reproducing the Project

```bash
git clone https://github.com/Anziya25/enterprise-rag-faiss-openai.git

cd enterprise-rag-faiss-openai

python3 -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

python app/main.py
```

Open a new terminal.

```bash
cd frontend

npm install

npm run dev
```

---

# Project Structure

```text
app/
frontend/
tests/
docs/
screenshots/
sample_documents/
README.md
requirements.txt
```

---

# License

This project is licensed under the MIT License.
