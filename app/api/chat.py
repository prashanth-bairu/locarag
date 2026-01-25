import time
from fastapi import APIRouter, Query

from app.rag.pipeline import RAGPipeline
from app.services.memory_service import get_memory

router = APIRouter()


@router.get("/")
def chat(query: str = Query(..., min_length=1), session_id: str = Query("default", min_length=1)) -> dict:
    start = time.perf_counter()
    pipeline = RAGPipeline(memory=get_memory(session_id))
    result = pipeline.run(query)
    latency_ms = round((time.perf_counter() - start) * 1000, 2)
    answer = result["answer"] or "I do not know based on the provided documents."
    return {
        "answer": answer,
        "session_id": session_id,
        "latency_ms": latency_ms,
        "retrieved_chunks": result["retrieved_chunks"],
    }
