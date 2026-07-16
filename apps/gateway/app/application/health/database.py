from sqlalchemy import text
from sqlalchemy.orm import Session


class DatabaseHealthService:
    """Service for checking database connectivity."""

    def check_connection(self, db: Session) -> bool:
        """Return True if the database connection is healthy."""
        db.execute(text("SELECT 1"))
        return True