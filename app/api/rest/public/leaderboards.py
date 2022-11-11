from __future__ import annotations

from typing import Optional

from fastapi import APIRouter
from fastapi import Depends
from fastapi import Query
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.responses import RedirectResponse

from app.api import dependencies
from app.api.rest.context import RequestContext
from app.common import responses
from app.common.templating import templates
from app.models.rework import Rework
from app.models.user import User
from app.usecases import reworks

router = APIRouter()


@router.get("/rework/{rework_id}", response_class=HTMLResponse)
async def rework_redirect(request: Request, rework_id: int):

    return RedirectResponse(f"/rework/{rework_id}/leaderboard?page=1", status_code=302)


@router.get("/rework/{rework_id}/leaderboard", response_class=HTMLResponse)
async def rework_leaderboard(
    request: Request,
    rework_id: int,
    page: int = Query(None),
    ctx: RequestContext = Depends(),
    user: Optional[User] = Depends(dependencies.get_user_from_cookie),
    nav_reworks: Optional[list[Rework]] = Depends(dependencies.get_navbar_reworks),
):

    if not page:
        return RedirectResponse(
            f"/rework/{rework_id}/leaderboard?page=1",
            status_code=302,
        )

    rework_data = await reworks.fetch_one(ctx, rework_id)
    if not isinstance(rework_data, Rework):
        return responses.flash("/", "Rework not found!", "error", request)

    return templates.TemplateResponse(
        "rework.html",
        {
            "request": request,
            "ctx": ctx,
            "user": user,
            "page_num": page,
            "nav_reworks": nav_reworks,
            "rework_data": rework_data,
        },
    )
