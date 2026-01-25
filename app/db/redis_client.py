from langchain_community.chat_message_histories import RedisChatMessageHistory
from app.core.config import settings


def get_message_history(session_id: str) -> RedisChatMessageHistory:
    return RedisChatMessageHistory(
        session_id=session_id,
        url=settings.redis_url,
        ttl=60 * 60 * 24,
    )
