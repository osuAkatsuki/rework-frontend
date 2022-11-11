from __future__ import annotations

from typing import Optional

from fastapi import Cookie
from fastapi import Depends

from app.api.rest.context import RequestContext
from app.models.rework import Rework
from app.models.user import User
from app.usecases import reworks
from app.usecases import users


async def get_user_from_cookie(
    ctx: RequestContext = Depends(),
    _id: str = Cookie(None, alias="user_id"),
) -> Optional[User]:
    if not _id:
        return None

    data = await users.fetch_one(ctx, int(_id))

    if isinstance(data, User):
        return data


async def get_navbar_reworks(ctx: RequestContext = Depends()) -> Optional[list[Rework]]:
    data = await reworks.fetch_all(ctx)

    if isinstance(data, list):
        return data
