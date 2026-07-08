from fastapi import FastAPI

from app.api.v1.router import api_router
from app.core.config import get_settings
from app.core.logging import configure_logging
import structlog
from contextlib import asynccontextmanager
from app.middleware.request_id import RequestIDMiddleware


settings = get_settings()
configure_logging()
logger = structlog.get_logger()

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Gateway starting", version=settings.app_version)
    yield
    logger.info("Gateway shutting down")


app = FastAPI(
    title=settings.app_name,
    description=settings.app_description,
    version=settings.app_version,
    lifespan=lifespan,
)

app.add_middleware(RequestIDMiddleware)

app.include_router(
    api_router,
    prefix=settings.api_prefix,
)


@app.get("/")
async def root():
    return {
        "application": settings.app_name,
        "version": settings.app_version,
        "status": "running",
    }