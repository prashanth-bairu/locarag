from langchain.memory import ConversationBufferMemory
from app.db.redis_client import get_message_history


def get_memory(session_id: str) -> ConversationBufferMemory:
    return ConversationBufferMemory(
        memory_key="chat_history",
        chat_memory=get_message_history(session_id),
        return_messages=True,
    )
