from __future__ import annotations

import os

from dotenv import load_dotenv

load_dotenv()


def read_bool(value: str) -> bool:
    return value.lower() in ("true", "1")


APP_ENV = os.environ["APP_ENV"]
APP_COMPONENT = os.environ["APP_COMPONENT"]
APP_HOST = os.environ["APP_HOST"]
APP_PORT = int(os.environ["APP_PORT"])

CODE_HOTRELOAD = read_bool(os.environ["CODE_HOTRELOAD"])
SERVICE_READINESS_TIMEOUT = int(os.environ["SERVICE_READINESS_TIMEOUT"])
PULL_SECRETS_FROM_VAULT = read_bool(os.environ["PULL_SECRETS_FROM_VAULT"])

PERFORMANCE_SERVICE_BASE_URL = os.environ["PERFORMANCE_SERVICE_BASE_URL"]
