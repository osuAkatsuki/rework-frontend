from __future__ import annotations

from typing import Any

from app.common import settings
from app.common.context import Context


class UsersRepo:
    BASE_URI = settings.PERFORMANCE_SERVICE_BASE_URL

    def __init__(self, ctx: Context) -> None:
        self.ctx = ctx

    async def fetch_one(self, user_id: int) -> dict[str, Any]:
        uri = f"{self.BASE_URI}/api/v1/reworks/users/{user_id}"
        resp = await self.ctx.http.get(uri)
        return resp.json()

    async def fetch_from_query(
        self,
        rework_id: int,
        query: str,
    ) -> list[dict[str, Any]]:
        uri = f"{self.BASE_URI}/api/v1/reworks/{rework_id}/users/search"
        resp = await self.ctx.http.get(
            uri,
            params={
                "query": query,
            },
        )
        return resp.json()
