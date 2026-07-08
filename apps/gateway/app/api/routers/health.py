from fastapi import APIRouter, Depends

from app.application.health.dto import HealthResponse
from app.application.health.service import HealthService
from app.dependencies.health import get_health_service

router = APIRouter(prefix="/health", tags=["Health"])


@router.get("", response_model=HealthResponse)
async def health(
    health_service: HealthService = Depends(get_health_service),
) -> HealthResponse:
    """Health check endpoint."""
    return health_service.get_health()