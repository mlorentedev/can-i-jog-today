from fastapi import Depends
from typing import Any, Dict, Optional

from app.core.config import get_settings
from app.core.logger import logger_config

from app.repositories.weather_repository import WeatherRepository

from app.cache.memcache import SimpleCache

log = logger_config(__name__)
settings = get_settings()


class WeatherService:

    def __init__(
        self, weather_repository: WeatherRepository = Depends(WeatherRepository)
    ):
        self.weather_repository = weather_repository
        self.cache = SimpleCache()

    async def get_weather(self, location: str) -> Optional[Dict[str, Any]]:
        cached_data = self.cache.get(location)
        if cached_data:
            log.info(f"Getting weather from cache for city: {location}")
            return cached_data
        try:
            log.info(f"Getting weather for city: {location}")
            weather = await self.weather_repository.get_weather(location)
            log.info(f"Got weather for city: {location}")

            # Business logic to determine if the weather is good

            self.cache.set(location, weather)
            return weather
        except Exception as e:
            log.error(f"Unexpected error getting weather for city: {location}")
            log.error(e)
            return {}
