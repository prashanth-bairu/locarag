from langchain.chains import ConversationalRetrievalChain


class RAGPipeline:
    def __init__(self, llm, retriever):
        self.chain = ConversationalRetrievalChain.from_llm(
            llm=llm,
            retriever=retriever,
            return_source_documents=True,
            verbose=True,
        )

    def run(self, query: str, chat_history=None):
        if chat_history is None:
            chat_history = []
        return self.chain.invoke({
            "question": query,
            "chat_history": chat_history,
        })
