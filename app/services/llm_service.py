from langchain_ollama import OllamaLLM
from app.core.config import settings


def get_llm() -> OllamaLLM:
    return OllamaLLM(model=settings.model_name)
