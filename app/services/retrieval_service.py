from app.core.config import settings
from app.db.vector_store import get_vector_store


def get_retriever():
    db = get_vector_store()
    return db.as_retriever(search_kwargs={"k": settings.retrieval_k})
