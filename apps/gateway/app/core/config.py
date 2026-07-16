from functools import lru_cache

from pydantic import computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings."""

    # -------------------------------------------------------------------------
    # Application
    # -------------------------------------------------------------------------
    app_name: str = "NextGen Data Engineering Platform"
    app_version: str = "0.1.0"
    app_description: str = "Enterprise AI Platform for Data Engineers"
    app_env: str = "development"
    debug: bool = True

    api_prefix: str = "/api/v1"

    # -------------------------------------------------------------------------
    # Database
    # -------------------------------------------------------------------------
    database_driver: str = "postgresql+psycopg"

    # Preferred for cloud environments (Neon, Azure, Railway, etc.)
    database_url: str | None = None

    # Fallback values for local development
    database_host: str = "localhost"
    database_port: int = 5432
    database_name: str = "postgres"
    database_user: str = "postgres"
    database_password: str = ""

    database_ssl_mode: str = "require"
    database_channel_binding: str = "require"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    @computed_field
    @property
    def sqlalchemy_database_uri(self) -> str:
        """
        Return the SQLAlchemy database connection URI.

        Priority:
        1. DATABASE_URL (recommended for cloud)
        2. Construct from individual database settings
        """
        if self.database_url:
            return self.database_url

        return (
            f"{self.database_driver}://"
            f"{self.database_user}:{self.database_password}@"
            f"{self.database_host}:{self.database_port}/"
            f"{self.database_name}"
            f"?sslmode={self.database_ssl_mode}"
            f"&channel_binding={self.database_channel_binding}"
        )

    @computed_field
    @property
    def is_production(self) -> bool:
        """Return True if the application is running in production."""
        return self.app_env.lower() == "production"
    

@lru_cache
def get_settings() -> Settings:
    """Return cached application settings."""
    return Settings()