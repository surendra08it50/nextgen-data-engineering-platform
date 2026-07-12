from datetime import datetime, UTC
import platform
import socket

from app.application.health.dto import HealthResponse
from app.core.app_info import app_info


class HealthService:
    """Application service for health checks."""

    def get_health(self) -> HealthResponse:
        """Return the current application health."""
        return HealthResponse(
            status="healthy",
            service="gateway",
            version=app_info.version,
            environment=app_info.environment,
            python_version=platform.python_version(),
            platform=platform.platform(),
            hostname=socket.gethostname(),
            timestamp=datetime.now(UTC).isoformat(),
        )