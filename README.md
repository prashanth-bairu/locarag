# locaRAG

A fully local Retrieval-Augmented Generation (RAG) system that lets you chat with your own documents — no cloud, no API keys, no data leaving your machine.

Built for personal use: load any PDF, ask questions in plain English, and get grounded answers backed by your documents with conversation memory across sessions.

---

## Features

- **Fully local** — LLM inference and embeddings run entirely on your machine via Ollama
- **PDF ingestion** — upload documents, they get chunked and indexed automatically
- **Semantic retrieval** — Chroma vector store finds the most relevant passages per query
- **Conversation memory** — Redis-backed session history so context carries across questions
- **Source transparency** — responses include the actual document chunks used to generate answers
- **Evaluation** — a Ragas-powered evaluator to measure retrieval and answer quality
- **Docker support** — spin up the full stack with one command

---

## Architecture

```text
Client → FastAPI → RAGPipeline
                       |
                       ├── Ollama LLM (llama3)
                       ├── Retriever → Chroma vector store
                       └── Redis session history

Upload → IngestionService → PDF Loader → Chunker → Chroma
```

---

## Project Structure

```text
app/
  api/          # FastAPI routes (chat, upload, health)
  core/         # config and logging
  db/           # Chroma and Redis clients
  models/       # Pydantic schemas
  rag/          # prompts, pipeline, chunking logic
  services/     # chat, ingestion, retrieval, LLM, memory
evaluation/     # Ragas dataset and evaluator script
scripts/        # helper utilities
tests/          # pytest tests
```

---

## Quick Start

### 1. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Pull models and start local services

```bash
# Pull LLM and embedding model
ollama pull llama3
ollama pull nomic-embed-text

# Start Redis
redis-server
```

### 4. Run the API

```bash
uvicorn main:app --reload
```

Swagger UI available at `http://127.0.0.1:8000/docs`

---

## API Usage

### Health check
```bash
curl http://127.0.0.1:8000/health
```

### Upload a PDF
```bash
curl -X POST http://127.0.0.1:8000/upload/ \
  -F "file=@/path/to/your.pdf"
```

### Ask a question
```bash
curl "http://127.0.0.1:8000/chat/?query=What+is+this+document+about&session_id=my-session"
```

Response includes `answer` and `contexts` (the source chunks used).

---

## Tests

```bash
pytest -q
```

---

## Evaluation

1. Add your test cases to `evaluation/dataset.json` (question, answer, contexts, ground_truth).
2. Run:

```bash
python evaluation/evaluator.py
```

Outputs faithfulness, answer relevancy, and context precision scores via Ragas.

---

## Docker

```bash
docker compose up --build
```

---

## Notes

- Everything runs offline after the initial model download.
- `session_id` query param isolates conversation history per user/session.
- Chat history is stored in Redis with a 1-hour TTL; swap to a persistent store if needed.
- Chroma persists to `chroma_db/` locally — delete it to reset the vector store.
