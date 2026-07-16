from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.application.health.database import DatabaseHealthService
from app.dependencies.database import get_db

router = APIRouter(
    prefix="/health/database",
    tags=["Database Health"],
)

database_health_service = DatabaseHealthService()


@router.get("")
async def database_health(
    db: Session = Depends(get_db),
):
    connected = database_health_service.check_connection(db)

    return {
        "status": "healthy",
        "database": "connected" if connected else "disconnected",
    }