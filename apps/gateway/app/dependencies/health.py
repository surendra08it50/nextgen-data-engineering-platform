from app.application.health.service import HealthService


def get_health_service() -> HealthService:
    """Return a HealthService instance."""
    return HealthService()