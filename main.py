#!/usr/bin/env python3

from __future__ import annotations

import logging

import uvicorn

from app.common import settings

try:
    __import__("uvloop").install()
except ImportError:
    pass


def main() -> int:
    # run the server
    uvicorn.run(
        "app.api_boot:api",
        host=settings.APP_HOST,
        port=settings.APP_PORT,
        reload=True,
        server_header=False,
        date_header=False,
    )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
