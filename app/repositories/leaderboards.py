from __future__ import annotations

from typing import Any

from app.common import settings
from app.common.context import Context


class LeaderboardsRepo:
    BASE_URI = settings.PERFORMANCE_SERVICE_BASE_URL

    def __init__(self, ctx: Context) -> None:
        self.ctx = ctx

    async def fetch_one(
        self,
        rework_id: int,
        page: int,
        limit: int = 50,
    ) -> dict[str, Any]:
        uri = f"{self.BASE_URI}/api/v1/reworks/{rework_id}/leaderboards"
        resp = await self.ctx.http.get(
            uri,
            params={
                "page": page,
                "amount": limit,
            },
        )
        return resp.json()
