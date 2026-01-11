from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader


def load_pdf(file_path: str):
    loader = PyPDFLoader(file_path)
    return loader.load()


from app.rag.chunking import split_documents


def chunk_pdf(file_path: str):
    return split_documents(load_pdf(file_path))
