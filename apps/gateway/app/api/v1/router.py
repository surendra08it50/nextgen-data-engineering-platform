from fastapi import APIRouter

from app.api.routers.health import router as health_router
from app.api.routers.database_health import router as database_health_router

api_router = APIRouter()

api_router.include_router(health_router)
api_router.include_router(database_health_router)