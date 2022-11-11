from __future__ import annotations

import hashlib

from fastapi import APIRouter
from fastapi import Cookie
from fastapi import Depends
from fastapi import Form
from fastapi import Request

from app.api.rest.context import RequestContext
from app.common import responses
from app.common.errors import ServiceError
from app.common.responses import Success
from app.models.session import LoginResponse
from app.models.session import QueueResponse
from app.usecases import sessions

router = APIRouter()


@router.post("/v1/sessions", response_model=Success[LoginResponse])
async def create(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
    ctx: RequestContext = Depends(),
):

    password_md5 = hashlib.md5(password.encode()).hexdigest()
    data = await sessions.create(ctx, username, password_md5)

    if isinstance(data, ServiceError):
        return responses.flash(
            "/auth/login",
            "Either username or password is wrong, please try again.",
            "error",
            request,
        )

    resp = responses.flash(
        "/",
        "Hey there, you are logged in, welcome back!",
        "success",
        request,
    )

    assert data.session_token is not None
    assert data.user_id is not None
    resp.set_cookie(key="session_token", value=data.session_token, expires=7200)
    resp.set_cookie(key="user_id", value=str(data.user_id), expires=7200)

    return resp


@router.post("/v1/sessions/queue", response_model=Success[QueueResponse])
async def enqueue(
    request: Request,
    rework_id: int = Form(...),
    session_token: str = Cookie(...),
    ctx: RequestContext = Depends(),
):
    data = await sessions.enqueue(ctx, rework_id, session_token)

    if isinstance(data, ServiceError):
        return responses.flash(
            f"/rework/{rework_id}/queue",
            data.value,
            "error",
            request,
        )

    return responses.flash(
        f"/rework/{rework_id}/leaderboard",
        "Added to queue!",
        "success",
        request,
    )


@router.get("/v1/sessions/remove", response_model=Success[list])
async def delete(
    request: Request,
    ctx: RequestContext = Depends(),
    session_token=Cookie(...),
):
    await sessions.delete(ctx, session_token)

    resp = responses.flash("/", "Successfully logged out!", "success", request)
    resp.delete_cookie(key="session_token")
    resp.delete_cookie(key="user_id")

    return resp
