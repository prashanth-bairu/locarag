from fastapi import FastAPI
from app.api.chat import router as chat_router
from app.api.health import router as health_router
from app.api.upload import router as upload_router

app = FastAPI(title="RAG GenAI System", version="0.1.0")
app.include_router(health_router)
app.include_router(upload_router, prefix="/upload", tags=["upload"])
app.include_router(chat_router, prefix="/chat", tags=["chat"])
