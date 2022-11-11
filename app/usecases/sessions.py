from __future__ import annotations

from typing import Union

from app.common.context import Context
from app.common.errors import ServiceError
from app.models.session import LoginResponse
from app.models.session import QueueResponse
from app.repositories.sessions import SessionsRepo


async def create(
    ctx: Context,
    username: str,
    password_md5: str,
) -> Union[LoginResponse, ServiceError]:

    s_repo = SessionsRepo(ctx)
    resp = await s_repo.create(username, password_md5)

    if not resp or not resp["success"]:
        return ServiceError.SESSIONS_INVALID_CREDENTIALS

    return LoginResponse.from_mapping(resp)


async def delete(ctx: Context, uuid_token: str) -> None:
    s_repo = SessionsRepo(ctx)
    await s_repo.delete(uuid_token)


async def enqueue(
    ctx: Context,
    rework_id: int,
    uuid_token: str,
) -> Union[QueueResponse, ServiceError]:
    s_repo = SessionsRepo(ctx)
    resp = await s_repo.enqueue(rework_id, uuid_token)

    if not resp:
        return ServiceError.SESSION_ENQUEUE_FAILED

    return QueueResponse.from_mapping(resp)
