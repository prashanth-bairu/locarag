# RAG GenAI System

A GitHub-ready, local-first RAG application for GenAI role portfolios.

## Features
- Local LLM inference with Ollama
- Local embeddings with Ollama (`nomic-embed-text`)
- PDF ingestion and chunking
- Chroma vector store for retrieval
- Redis-backed session memory
- FastAPI service layer with modular architecture
- Evaluation script using Ragas
- Basic tests with pytest
- Docker and docker-compose support
- Logging and latency tracking

## Architecture
```text
Client -> FastAPI -> ChatService -> RAGPipeline
                           |          |\
                           |          | -> Ollama LLM
                           |          | -> Retriever -> Chroma
                           |          \
                           |           -> Redis memory
                           \
                            -> IngestionService -> PDF Loader -> Chunker -> Chroma
```

## Project Structure
```text
app/
  api/        # routes
  core/       # config + logging
  db/         # Chroma + Redis clients
  models/     # Pydantic schemas
  rag/        # prompts + pipeline + chunking
  services/   # chat/ingestion/retrieval/llm/memory
evaluation/   # ragas dataset + evaluator
scripts/      # helper scripts
tests/        # basic tests
```

## Quick Start
### 1) Create a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
```

### 2) Install Python dependencies
```bash
pip install -r requirements.txt
```

### 3) Start local dependencies
```bash
# Ollama models
ollama pull llama3
ollama pull nomic-embed-text

# Redis
redis-server
```

### 4) Run the API
```bash
uvicorn main:app --reload
```

Open the docs at `http://127.0.0.1:8000/docs`

## API Usage
### Health check
```bash
curl http://127.0.0.1:8000/health
```

### Upload a PDF
```bash
curl -X POST http://127.0.0.1:8000/upload/ \
  -F "file=@/absolute/path/to/your.pdf"
```

### Ask a question
```bash
curl "http://127.0.0.1:8000/chat/?query=What%20is%20this%20document%20about%3F&session_id=demo-user"
```

## Tests
```bash
pytest -q
```

## Evaluation
1. Update `evaluation/dataset.json` with question, answer, contexts, and ground truth.
2. Run:
```bash
python evaluation/evaluator.py
```

## Docker
```bash
docker compose up --build
```

## Notes
- This project is designed to be fully local and offline after model download.
- The final codebase is intentionally modular for interview discussion around architecture and extensibility.
