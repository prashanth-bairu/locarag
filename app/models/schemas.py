from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    status: str = Field(..., examples=["ok"])


class UploadResponse(BaseModel):
    message: str
    filename: str
    chunks_indexed: int


class ChatRequest(BaseModel):
    query: str
    session_id: str = "default"


class ChatResponse(BaseModel):
    answer: str
    session_id: str
    latency_ms: float
    retrieved_chunks: int
