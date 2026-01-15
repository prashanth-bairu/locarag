from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "RAG GenAI System"
    model_name: str = "llama3"
    embedding_model: str = "nomic-embed-text"  # local embedding model via ollama
    redis_url: str = "redis://localhost:6379"
    chroma_path: str = "chroma_db"
    data_path: str = "data"
    retrieval_k: int = 4
    chunk_size: int = 900
    chunk_overlap: int = 180

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
