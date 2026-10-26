# DocPilot frontend

React + TypeScript + Vite interface for the DocPilot document RAG application.

## Run locally

First start the backend and Ollama using the [root README](../README.md).

```bash
cd frontend
npm ci
npm run dev
```

The development UI normally runs at http://localhost:5173. The backend's CORS configuration allows this origin.

## Quality checks

```bash
npm run lint
npm run build
```

The frontend uses Vite, React, TypeScript, and Tailwind CSS. These commands are documented but were not executed as part of this README update.
