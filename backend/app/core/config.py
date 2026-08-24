from pathlib import Path

from dotenv import load_dotenv
from pydantic_settings import BaseSettings


BASE_DIR = Path(__file__).resolve().parents[3]

load_dotenv(BASE_DIR / ".env")


class Settings(BaseSettings):
    cognodb_uri: str
    cognodb_username: str
    cognodb_password: str

    frontend_url: str = ""

    class Config:
        env_file = BASE_DIR / ".env"
        extra = "ignore"


settings = Settings()