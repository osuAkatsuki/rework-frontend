from __future__ import annotations

from typing import Union

from app.common.context import Context
from app.common.errors import ServiceError
from app.models.leaderboard import Leaderboard
from app.repositories.leaderboards import LeaderboardsRepo


async def fetch_one(
    ctx: Context,
    rework_id: int,
    page: int,
    limit: int = 50,
) -> Union[Leaderboard, ServiceError]:
    l_repo = LeaderboardsRepo(ctx)
    resp = await l_repo.fetch_one(rework_id, page, limit)

    if not resp:
        return ServiceError.LEADERBOARDS_NOT_FOUND

    return Leaderboard.from_mapping(resp)
