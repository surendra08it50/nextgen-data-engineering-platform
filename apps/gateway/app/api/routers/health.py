from fastapi import APIRouter, Depends

from app.application.health.dto import HealthResponse
from app.application.health.service import HealthService
from app.dependencies.health import get_health_service
from common.responses.base import ApiResponse

router = APIRouter(prefix="/health", tags=["Health"])


@router.get("", response_model=ApiResponse[HealthResponse])
async def health(
    health_service: HealthService = Depends(get_health_service),
) -> ApiResponse[HealthResponse]:
    """Health check endpoint."""
    return ApiResponse(
        data=health_service.get_health(),
    )