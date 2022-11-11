from __future__ import annotations

from typing import Optional

from fastapi import APIRouter
from fastapi import Depends
from fastapi import Request
from fastapi.responses import HTMLResponse

from app.api import dependencies
from app.api.rest.context import RequestContext
from app.common.templating import templates
from app.models.rework import Rework
from app.models.user import User

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def homepage(
    request: Request,
    ctx: RequestContext = Depends(),
    user: Optional[User] = Depends(dependencies.get_user_from_cookie),
    nav_reworks: Optional[list[Rework]] = Depends(dependencies.get_navbar_reworks),
):

    return templates.TemplateResponse(
        "homepage.html",
        {"request": request, "ctx": ctx, "user": user, "nav_reworks": nav_reworks},
    )
