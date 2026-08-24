from pathlib import Path

from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict


# Project root directory
BASE_DIR = Path(__file__).resolve().parents[3]

# Load environment variables
load_dotenv(BASE_DIR / ".env")


class Settings(BaseSettings):
    cognodb_uri: str
    cognodb_username: str
    cognodb_password: str

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        extra="ignore"
    )


settings = Settings()