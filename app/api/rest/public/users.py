from __future__ import annotations

from typing import Optional

from fastapi import APIRouter
from fastapi import Depends
from fastapi import Request
from fastapi.responses import HTMLResponse

from app.api import dependencies
from app.api.rest.context import RequestContext
from app.common import responses
from app.common.templating import templates
from app.models.rework import Rework
from app.models.stats import UserStats
from app.models.user import User
from app.usecases import reworks
from app.usecases import stats

router = APIRouter()


@router.get("/rework/{rework_id}/users/{user_id}", response_class=HTMLResponse)
async def rework_user(
    request: Request,
    rework_id: int,
    user_id: int,
    ctx: RequestContext = Depends(),
    user: Optional[User] = Depends(dependencies.get_user_from_cookie),
    nav_reworks: Optional[list[Rework]] = Depends(dependencies.get_navbar_reworks),
):

    rework_data = await reworks.fetch_one(ctx, rework_id)
    if not isinstance(rework_data, Rework):
        return responses.flash("/", "Rework not found!", "error", request)

    user_data = await stats.fetch_one(ctx, user_id, rework_id)
    if not isinstance(user_data, UserStats):
        return responses.flash("/", "User not found!", "error", request)

    return templates.TemplateResponse(
        "profile.html",
        {
            "request": request,
            "ctx": ctx,
            "user": user,
            "nav_reworks": nav_reworks,
            "rework_data": rework_data,
            "user_data": user_data,
        },
    )
