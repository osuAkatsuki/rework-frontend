from __future__ import annotations

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from shared_modules import logger
from starlette.middleware.base import BaseHTTPMiddleware

from app.api import middlewares
from app.services import http


def init_http(api: FastAPI) -> None:
    @api.on_event("startup")
    async def startup_http() -> None:
        logger.info("Starting up http connector")
        service_http = http.ServiceHTTP()
        api.state.http = service_http
        logger.info("HTTP connector started up")

    @api.on_event("shutdown")
    async def shutdown_http() -> None:
        logger.info("Shutting down http connector")
        await api.state.http.aclose()
        del api.state.http
        logger.info("HTTP connector shut down")


def init_middlewares(api: FastAPI) -> None:
    middleware_stack = [
        middlewares.add_http_to_request,
    ]
    # NOTE: starlette reverses the order of the middleware stack
    # more info: https://github.com/encode/starlette/issues/479
    for middleware in reversed(middleware_stack):
        api.add_middleware(BaseHTTPMiddleware, dispatch=middleware)


def init_routes(api: FastAPI) -> None:
    from .v1 import router as v1_router
    from .public import router as public_router

    api.mount("/static", StaticFiles(directory="web/static"), name="static")

    api.include_router(v1_router)
    api.include_router(public_router)

    @api.get("/_health")
    async def healthcheck():
        return {"status": "ok"}


def init_api():
    api = FastAPI()

    init_http(api)
    init_middlewares(api)
    init_routes(api)

    return api
