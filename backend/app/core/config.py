import os

from dotenv import load_dotenv

from pydantic_settings import BaseSettings

load_dotenv(os.path.join(os.path.dirname(__file__), "../../.env"))


class Settings(BaseSettings):
    LOG_LEVEL: str
    AUTHOR: str
    CONTACT: str
    DESCRIPTION: str
    IMAGE_NAME: str
    IMAGE_VERSION: str
    HOST: str
    PORT: int
    API_PREFIX: str
    DOC_URL: str
    REDOC_URL: str
    WEATHER_API_KEY: str
    WEATHER_API_URL: str
    IMAGES_API_URL: str
    IMAGES_API_KEY: str

    class Config:
        env_file = os.getenv("ENV_FILE", ".env")
        env_file_encoding = "utf-8"
        extra = "ignore"


def get_settings() -> Settings:
    return Settings()
