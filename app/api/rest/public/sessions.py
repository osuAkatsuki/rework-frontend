from __future__ import annotations

from typing import Optional

from fastapi import APIRouter
from fastapi import Cookie
from fastapi import Depends
from fastapi import Request
from fastapi.responses import HTMLResponse

from app.api import dependencies
from app.api.rest.context import RequestContext
from app.common import responses
from app.common.templating import templates
from app.models.rework import Rework
from app.models.user import User
from app.usecases import reworks

router = APIRouter()


@router.get("/auth/login", response_class=HTMLResponse)
async def login(
    request: Request,
    ctx: RequestContext = Depends(),
    user: Optional[User] = Depends(dependencies.get_user_from_cookie),
    nav_reworks: Optional[list[Rework]] = Depends(dependencies.get_navbar_reworks),
):

    return templates.TemplateResponse(
        "login.html",
        {"request": request, "ctx": ctx, "user": user, "nav_reworks": nav_reworks},
    )


@router.get("/rework/{rework_id}/queue", response_class=HTMLResponse)
async def rework_queue(
    request: Request,
    rework_id: int,
    ctx: RequestContext = Depends(),
    session_token: str = Cookie(None),
    user: Optional[User] = Depends(dependencies.get_user_from_cookie),
    nav_reworks: Optional[list[Rework]] = Depends(dependencies.get_navbar_reworks),
):

    if not user:
        return responses.flash(
            "/auth/login",
            "You must be logged in!",
            "error",
            request,
        )

    rework_data = await reworks.fetch_one(ctx, rework_id)
    if not isinstance(rework_data, Rework):
        return responses.flash("/", "Rework not found!", "error", request)

    return templates.TemplateResponse(
        "queue.html",
        {
            "request": request,
            "ctx": ctx,
            "user": user,
            "nav_reworks": nav_reworks,
            "rework_data": rework_data,
            "session_token": session_token,
        },
    )
