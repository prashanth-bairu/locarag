from fastapi import APIRouter, HTTPException
from app.services.llm_service import get_llm
from app.services.retrieval_service import get_retriever
from app.services.memory_service import load_chat_history, save_chat_turn
from app.rag.pipeline import RAGPipeline

router = APIRouter()


@router.get("/")
def chat(query: str, session_id: str = "default"):
    try:
        llm = get_llm()
        retriever = get_retriever()
        chat_history = load_chat_history(session_id)

        pipeline = RAGPipeline(llm, retriever)
        result = pipeline.run(query, chat_history=chat_history)

        answer = result.get("answer", "")
        source_documents = result.get("source_documents", [])

        save_chat_turn(session_id, query, answer)

        return {
            "answer": answer,
            "contexts": [doc.page_content for doc in source_documents],
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Chat failed: {type(e).__name__}: {e}")
