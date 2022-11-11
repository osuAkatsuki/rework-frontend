from __future__ import annotations

from typing import Union

from app.common.context import Context
from app.common.errors import ServiceError
from app.models.stats import UserStats
from app.repositories.stats import StatsRepo


async def fetch_one(
    ctx: Context,
    user_id: int,
    rework_id: int,
) -> Union[UserStats, ServiceError]:
    s_repo = StatsRepo(ctx)
    resp = await s_repo.fetch_one(user_id, rework_id)

    if not resp:
        return ServiceError.STATS_NOT_FOUND

    return UserStats.from_mapping(resp)
