import pytest
from httpx import AsyncClient, ASGITransport

from app.core.config import get_settings
from app.main import app

settings = get_settings()


@pytest.mark.asyncio
async def test_weather_by_city():
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url=f"http://{settings.HOST}:{settings.PORT}/{settings.API_PREFIX}",
    ) as client:
        response = await client.get("/weather/city?q=Sevilla")
    assert response.status_code == 200
    assert response.json() == {"city": "Sevilla"}


@pytest.mark.asyncio
async def test_weather_by_city_not_found():
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url=f"http://{settings.HOST}:{settings.PORT}/{settings.API_PREFIX}",
    ) as client:
        response = await client.get("/weather/city?q=UnknownCity")
    assert response.status_code == 404
    assert response.json() == {"detail": "City not found"}
