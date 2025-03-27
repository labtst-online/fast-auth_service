import os
from typing import Any

from pydantic import PostgresDsn, field_validator
from pydantic_core import MultiHostUrl
from pydantic_core.core_schema import ValidationInfo
from pydantic_settings import BaseSettings, SettingsConfigDict

# Determine the path to the .env file relative to this config file's location
# This goes up two levels from core/ to the auth/ directory
# You might adjust this based on where you run the app / load env vars from
env_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), '.env')

class Settings(BaseSettings):
    # Load .env file if it exists
    model_config = SettingsConfigDict(env_file=env_path, extra='ignore')

    APP_ENV: str = "development" # Default to development

    # Postgres Database Config
    POSTGRES_SERVER: str
    POSTGRES_PORT: int = 5432
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

    # --- Async SQLAlchemy Database URL ---
    # Populated by a validator below
    ASYNC_SQLALCHEMY_DATABASE_URI: PostgresDsn | None = None

    @field_validator("ASYNC_SQLALCHEMY_DATABASE_URI", mode="before")
    @classmethod
    def assemble_async_db_connection(cls, v: str | None, info: ValidationInfo) -> Any:
        if isinstance(v, str):
            # If the URI is already provided as a string, use it directly
            return v
        # Otherwise, build it from components
        values = info.data
        return MultiHostUrl.build(
            scheme="postgresql+asyncpg",  # Use asyncpg driver
            username=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_SERVER"),
            port=values.get("POSTGRES_PORT"),
            path=f"{values.get('POSTGRES_DB') or ''}",
        )

    # --- Sync SQLAlchemy Database URL (for Alembic) ---
    # Populated by a validator below
    SYNC_SQLALCHEMY_DATABASE_URI: PostgresDsn | None = None

    @field_validator("SYNC_SQLALCHEMY_DATABASE_URI", mode="before")
    @classmethod
    def assemble_sync_db_connection(cls, v: str | None, info: ValidationInfo) -> Any:
        if isinstance(v, str):
            return v
        values = info.data
        # Use psycopg2 driver for Alembic's sync operations
        # Make sure 'psycopg2-binary' is installed
        return MultiHostUrl.build(
            scheme="postgresql+psycopg2",
            username=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_SERVER"),
            port=values.get("POSTGRES_PORT"),
            path=f"{values.get('POSTGRES_DB') or ''}",
        )

settings = Settings()
