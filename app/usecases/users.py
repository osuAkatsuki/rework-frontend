from __future__ import annotations

from typing import Union

from app.common.context import Context
from app.common.errors import ServiceError
from app.models.user import User
from app.models.user import UserQuery
from app.repositories.users import UsersRepo


async def fetch_one(ctx: Context, user_id: int) -> Union[User, ServiceError]:
    u_repo = UsersRepo(ctx)
    resp = await u_repo.fetch_one(user_id)

    if not resp:
        return ServiceError.USERS_NOT_FOUND

    return User.from_mapping(resp)


async def search(
    ctx: Context,
    rework_id: int,
    query: str,
) -> Union[list[UserQuery], ServiceError]:
    u_repo = UsersRepo(ctx)
    resp = await u_repo.fetch_from_query(rework_id, query)

    if not resp:
        return ServiceError.USERS_NOT_FOUND

    return [UserQuery.from_mapping(user) for user in resp]
