import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.logger import logger_config
from app.core.config import get_settings

from app.routes.health_router import health_router
from app.routes.weather_router import weather_router

log = logger_config(__name__)
settings = get_settings()


def init_app():
    log.info("Starting application")
    log.info(f"Author: {settings.AUTHOR}")
    log.info(f"Contact: {settings.CONTACT}")
    log.info(f"Description: {settings.DESCRIPTION}")
    log.info(f"Image Name: {settings.IMAGE_NAME}")
    log.info(f"Image Version: {settings.IMAGE_VERSION}")
    log.info(f"Host: {settings.HOST}")
    log.info(f"Port: {settings.PORT}")
    log.info(f"API Prefix: {settings.API_PREFIX}")
    log.info(f"Doc URL: {settings.DOC_URL}")
    log.info(f"Redoc URL: {settings.REDOC_URL}")
    log.info(f"Images API URL: {settings.IMAGES_API_URL}")
    log.info(f"Weather API URL: {settings.WEATHER_API_URL}")

    app = FastAPI(
        title=settings.IMAGE_NAME,
        version=settings.IMAGE_VERSION,
        openapi_url=f"{settings.API_PREFIX}/openapi.json",
        docs_url=settings.DOC_URL,
        redoc_url=settings.REDOC_URL,
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(health_router)
    app.include_router(weather_router, prefix=settings.API_PREFIX)

    log.info("Application started successfully")

    return app


app = init_app()


def run():
    uvicorn.run("app.main:app", host=settings.HOST, port=settings.PORT, reload=True)


if __name__ == "__main__":
    run()
