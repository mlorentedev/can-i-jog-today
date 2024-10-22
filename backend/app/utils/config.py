import os

from dotenv import load_dotenv

from pydantic_settings import BaseSettings

load_dotenv(os.path.join(os.path.dirname(__file__), "../../.env"))

class Settings(BaseSettings):
    WEATHER_API_KEY : str
    WEATHER_API_URL : str

    @property
    def weather_api_key(self) -> str:
        return os.getenv("WEATHER_API_KEY")
    
    @property
    def weather_api_url(self) -> str:
        return os.getenv("WEATHER_API_URL")
    
    class Config:
        env_file = os.getenv("ENV_FILE", ".env")
        env_file_encoding = "utf-8"
        extra = "ignore"


def get_settings() -> Settings:
    return Settings()