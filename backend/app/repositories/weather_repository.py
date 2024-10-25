import httpx

from app.core.logger import logger_config
from app.core.config import get_settings

log = logger_config(__name__)
settings = get_settings()


class WeatherRepository:

    def __init__(self):
        self.weather_api_url = settings.WEATHER_API_URL
        self.weather_api_key = settings.WEATHER_API_KEY

    async def get_weather(self, location: str):
        if not location:
            raise ValueError("Location is required")
        try:
            params = {
                "q": location,
                "appid": self.weather_api_key,
                "units": "metric",
            }
            log.info(f"Fetching weather for city: {location}")
            async with httpx.AsyncClient() as client:
                response = await client.get(self.weather_api_url, params=params)
            response.raise_for_status()
            if response.status_code == 404:
                log.error(f"City not found: {location}")
                return {}
            elif response.status_code != 200:
                log.error(f"Error fetching weather for city: {location}")
                return {}
            weather = response.json()
            log.info(f"Got weather for city: {location}")
            return weather
        except httpx.HTTPStatusError as e:
            log.error(f"Error fetching weather for city: {location}")
            log.error(e)
        except Exception as e:
            log.error(f"Unexpected error getting weather for city: {location}")
            log.error(e)
        return {}
