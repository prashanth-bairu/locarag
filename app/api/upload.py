from pathlib import Path
from fastapi import APIRouter, File, UploadFile
from app.core.config import settings

router = APIRouter()
Path(settings.data_path).mkdir(parents=True, exist_ok=True)


@router.post("/")
async def upload(file: UploadFile = File(...)) -> dict:
    safe_name = Path(file.filename).name
    destination = Path(settings.data_path) / safe_name
    with destination.open("wb") as output:
        contents = await file.read()
    output.write(contents)
    from app.services.ingestion_service import load_pdf
    docs = load_pdf(str(destination))
    return {"message": "uploaded", "filename": safe_name, "chunks_indexed": len(docs)}
