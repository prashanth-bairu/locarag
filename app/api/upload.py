from pathlib import Path
from fastapi import APIRouter, File, HTTPException, UploadFile
from app.core.config import settings
from app.services.ingestion_service import ingest_pdf

router = APIRouter()
Path(settings.data_path).mkdir(parents=True, exist_ok=True)


@router.post("/")
async def upload(file: UploadFile = File(...)) -> dict:
    if not file.filename:
        raise HTTPException(status_code=400, detail="Filename is required")
    safe_name = Path(file.filename).name
    destination = Path(settings.data_path) / safe_name
    contents = await file.read()
    with destination.open("wb") as output:
        output.write(contents)
    chunks_indexed = ingest_pdf(str(destination))
    return {
        "message": "File processed successfully",
        "filename": safe_name,
        "chunks_indexed": chunks_indexed,
    }
