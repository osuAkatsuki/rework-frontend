from __future__ import annotations

from typing import Union

from app.common.context import Context
from app.common.errors import ServiceError
from app.models.rework import Rework
from app.repositories.reworks import ReworksRepo


async def fetch_one(ctx: Context, rework_id: int) -> Union[Rework, ServiceError]:
    r_repo = ReworksRepo(ctx)
    resp = await r_repo.fetch_one(rework_id)

    if not resp:
        return ServiceError.REWORKS_NOT_FOUND

    return Rework.from_mapping(resp)


async def fetch_all(ctx: Context) -> Union[list[Rework], ServiceError]:
    r_repo = ReworksRepo(ctx)
    resp = await r_repo.fetch_all()

    if not resp:
        return ServiceError.REWORKS_NOT_FOUND

    return [Rework.from_mapping(rework) for rework in resp]
