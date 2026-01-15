from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader


def load_pdf(file_path: str):
    loader = PyPDFLoader(file_path)
    return loader.load()


from app.rag.chunking import split_documents


def chunk_pdf(file_path: str):
    return split_documents(load_pdf(file_path))



def count_empty_chunks(chunks):
    return sum(1 for chunk in chunks if not getattr(chunk, "page_content", "").strip())


from app.db.vector_store import get_vector_store


def ingest_pdf(file_path: str) -> int:
    chunks = chunk_pdf(file_path)
    db = get_vector_store()
    db.add_documents(chunks)
    return len(chunks)
