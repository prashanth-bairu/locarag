import logging
import time
from app.rag.pipeline import RAGPipeline
from app.services.memory_service import get_memory


logger = logging.getLogger(__name__)


class ChatService:
    def run(self, query: str, session_id: str) -> dict:
        logger.info("chat request started | session_id=%s", session_id)
        start = time.perf_counter()
        pipeline = RAGPipeline(memory=get_memory(session_id))
        result = pipeline.run(query)
        latency_ms = round((time.perf_counter() - start) * 1000, 2)
        answer = result["answer"] or "I do not know based on the provided documents."
        logger.info("chat request finished | session_id=%s | latency_ms=%s", session_id, latency_ms)
        return {
            "answer": answer,
            "session_id": session_id,
            "latency_ms": latency_ms,
            "retrieved_chunks": result["retrieved_chunks"],
            "contexts": result["contexts"],
        }
