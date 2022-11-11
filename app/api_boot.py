from __future__ import annotations

from shared_modules import logger

from app.api.rest import init_api
from app.common import settings

logger.configure_logging(app_env=settings.APP_ENV, log_level=settings.LOG_LEVEL)

api = init_api()
