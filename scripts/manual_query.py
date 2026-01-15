from app.db.vector_store import get_vector_store


if __name__ == "__main__":
    docs = get_vector_store().similarity_search("test", k=2)
    print(f"retrieved={len(docs)}")
