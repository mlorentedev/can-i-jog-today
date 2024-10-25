from fastapi import APIRouter, HTTPException

from app.services import weather_service

weather_router = APIRouter()


@weather_router.get(
    "/weather/{location}",
    tags=["Weather"],
    responses={
        200: {"description": "Get weather information of a city"},
        404: {"description": "City not found"},
    },
)
async def get_weather(location: str):
    try:
        weather_info = await weather_service.get_weather(location)
        return weather_info
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
