from app.core.config import get_settings

settings = get_settings()


class AppInfo:
    """Application metadata."""

    name = settings.app_name
    version = settings.app_version
    environment = settings.app_env


app_info = AppInfo()