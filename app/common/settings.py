from __future__ import annotations

import os

from dotenv import load_dotenv

load_dotenv()

LOG_LEVEL = int(os.environ["LOG_LEVEL"])

APP_ENV = os.environ["APP_ENV"]
APP_COMPONENT = os.environ["APP_COMPONENT"]
APP_HOST = os.environ["APP_HOST"]
APP_PORT = int(os.environ["APP_PORT"])

API_PORT = int(os.environ["API_PORT"])
