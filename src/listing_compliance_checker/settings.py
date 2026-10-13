"""Reads my API keys and other settings from the .env file."""

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Everything the project needs to run. Values come from .env,
    and it stops straight away if one is missing."""

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
    anthropic_api_key: SecretStr
    openai_api_key: SecretStr
