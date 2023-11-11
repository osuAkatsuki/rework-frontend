#!/usr/bin/env python3

from __future__ import annotations
import atexit

import uvicorn

from app.common import settings
import app.logging
import app.exception_handling

try:
    __import__("uvloop").install()
except ImportError:
    pass


def main() -> int:
    app.logging.configure_logging()

    app.exception_handling.hook_exception_handlers()
    atexit.register(app.exception_handling.unhook_exception_handlers)

    # run the server
    uvicorn.run(
        "app.api_boot:api",
        host=settings.APP_HOST,
        port=settings.APP_PORT,
        reload=settings.CODE_HOTRELOAD,
        server_header=False,
        date_header=False,
    )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
