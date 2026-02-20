from app.core.config import Settings


def test_default_settings() -> None:
    settings = Settings()
    assert settings.model_name
    assert settings.embedding_model
    assert settings.redis_url.startswith("redis://")
