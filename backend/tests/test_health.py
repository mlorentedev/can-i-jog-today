import pytest
from httpx import AsyncClient, ASGITransport

from app.core.config import get_settings
from app.main import app

settings = get_settings()


@pytest.mark.asyncio
async def test_health_check():
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url=f"http://{settings.HOST}:{settings.PORT}",
    ) as client:
        response = await client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
