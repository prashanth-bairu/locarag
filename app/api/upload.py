from pathlib import Path
from fastapi import APIRouter, File, UploadFile
from app.core.config import settings

router = APIRouter()
Path(settings.data_path).mkdir(parents=True, exist_ok=True)


@router.post("/")
async def upload(file: UploadFile = File(...)) -> dict:
    destination = Path(settings.data_path) / file.filename
    with destination.open("wb") as output:
        output.write(await file.read())
    return {"message": "uploaded", "filename": file.filename, "chunks_indexed": 0}
