from fastapi import APIRouter

from app.application.health.dto import HealthResponse
from app.application.health.service import HealthService

router = APIRouter(prefix="/health", tags=["Health"])

health_service = HealthService()


@router.get("", response_model=HealthResponse)
async def health() -> HealthResponse:
    """Health check endpoint."""
    return health_service.get_health()