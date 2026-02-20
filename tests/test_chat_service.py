from app.services.chat_service import ChatService


class DummyPipeline:
    def run(self, query: str):
        return {
            "answer": f"echo::{query}",
            "retrieved_chunks": 2,
            "contexts": ["a", "b"],
        }


def test_chat_service(monkeypatch):
    service = ChatService()

    monkeypatch.setattr("app.services.chat_service.get_memory", lambda session_id: None)
    monkeypatch.setattr("app.services.chat_service.RAGPipeline", lambda memory=None: DummyPipeline())

    result = service.run("hello", "s1")
    assert result["answer"] == "echo::hello"
    assert result["retrieved_chunks"] == 2
    assert result["session_id"] == "s1"
