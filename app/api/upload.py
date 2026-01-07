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
    return {"message": "uploaded", "filename": safe_name, "chunks_indexed": 0}
