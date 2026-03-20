from app.db.redis_client import get_redis_history


def get_history(session_id: str):
    return get_redis_history(session_id)


def load_chat_history(session_id: str):
    history = get_redis_history(session_id)
    return history.messages


def save_chat_turn(session_id: str, question: str, answer: str):
    history = get_redis_history(session_id)
    history.add_user_message(question)
    history.add_ai_message(answer)
