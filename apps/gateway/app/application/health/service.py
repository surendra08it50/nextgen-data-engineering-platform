from app.application.health.dto import HealthResponse


class HealthService:
    """Application service for health checks."""

    def get_health(self) -> HealthResponse:
        """Return the current application health."""
        return HealthResponse(
            status="healthy",
            service="gateway",
        )