from langchain.chains import ConversationalRetrievalChain
from app.services.llm_service import get_llm
from app.services.retrieval_service import get_retriever


class RAGPipeline:
    def __init__(self, memory=None):
        self.chain = ConversationalRetrievalChain.from_llm(
            llm=get_llm(),
            retriever=get_retriever(),
            memory=memory,
            return_source_documents=True,
        )

    def run(self, query: str) -> dict:
        result = self.chain.invoke({"question": query})
        docs = result.get("source_documents", [])
        return {
            "answer": result["answer"],
            "retrieved_chunks": len(docs),
            "contexts": [doc.page_content for doc in docs],
        }
