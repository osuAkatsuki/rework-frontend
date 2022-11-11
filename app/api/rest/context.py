from __future__ import annotations

from fastapi import Request

from app.common.context import Context
from app.services import http


class RequestContext(Context):
    def __init__(self, request: Request) -> None:
        self.request = request

    @property
    def http(self) -> http.ServiceHTTP:
        return self.request.state.http
