from pydantic import BaseModel


class HealthResponse(BaseModel):
    """Health check response."""

    status: str
    service: str
    version: str
    environment: str
    python_version: str
    platform: str
    hostname: str
    timestamp: str