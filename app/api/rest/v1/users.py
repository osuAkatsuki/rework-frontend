from __future__ import annotations

from fastapi import APIRouter
from fastapi import Depends

from app.api.rest.context import RequestContext
from app.common import responses
from app.common.errors import ServiceError
from app.common.responses import Success
from app.models.user import User
from app.models.user import UserQuery
from app.usecases import users

router = APIRouter()


@router.get("/v1/users/{user_id}", response_model=Success[User])
async def get_user(user_id: int, ctx: RequestContext = Depends()):
    data = await users.fetch_one(ctx, user_id)
    if isinstance(data, ServiceError):
        return responses.failure(data, "Failed to fetch user")

    return responses.success(data)


@router.get("/v1/users", response_model=Success[list[UserQuery]])
async def search_users(
    query: str,
    rework_id: int,
    ctx: RequestContext = Depends(),
):
    data = await users.search(ctx, rework_id, query)
    if isinstance(data, ServiceError):
        return responses.failure(data, "Failed to search users")

    return responses.success(data)
