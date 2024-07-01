from __future__ import annotations

from typing import Any
from typing import Generic
from typing import Literal
from typing import TypeVar
from typing import Union

import orjson
from fastapi import Request
from fastapi.responses import RedirectResponse
from pydantic import BaseModel

from app.common import json
from app.common.errors import ServiceError

T = TypeVar("T")


class Success(BaseModel, Generic[T]):
    status: Literal["success"]
    data: T


def success(
    content: Any,
    status_code: int = 200,
    headers: Union[dict, None] = None,
) -> json.ORJSONResponse:
    data = {"status": "success", "data": content}
    return json.ORJSONResponse(data, status_code, headers)


class ErrorResponse(BaseModel, Generic[T]):
    status: Literal["error"]
    error: T
    message: str


def failure(
    error: ServiceError,
    message: str,
    status_code: int = 400,
    headers: Union[dict, None] = None,
) -> json.ORJSONResponse:
    data = {"status": "error", "error": error, "message": message}
    return json.ORJSONResponse(data, status_code, headers)


def flash(
    path: str,
    message: str,
    state: str,
    request: Request,
):
    """Flash a message to the user"""

    # This is a hack to get around the fact that FastAPI doesn't support
    # sessions in the sense we need, so we have to use a cookie instead.

    resp = RedirectResponse(path, status_code=302)
    errors = []

    cookie_errors = request.cookies.get("errors", None)
    if cookie_errors is not None:
        errors.extend(orjson.loads(cookie_errors))

    errors.append({"state": state, "message": message, "path": path})
    resp.set_cookie("errors", orjson.dumps(errors).decode(), expires=4)
    return resp
