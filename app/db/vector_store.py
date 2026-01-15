from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from app.core.config import settings


def get_embedding_model() -> OllamaEmbeddings:
    return OllamaEmbeddings(model=settings.embedding_model)


def get_vector_store() -> Chroma:
    return Chroma(
        persist_directory=settings.chroma_path,
        embedding_function=get_embedding_model(),
    )
