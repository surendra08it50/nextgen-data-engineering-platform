from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings."""

    app_name: str = "NextGen Data Engineering Platform"
    app_version: str = "0.1.0"
    app_description: str = "Enterprise AI Platform for Data Engineers"

    api_prefix: str = "/api/v1"

    debug: bool = True

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    """Return cached application settings."""
    return Settings()