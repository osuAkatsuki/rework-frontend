from __future__ import annotations

from typing import Any

from app.common import settings
from app.common.context import Context


class ScoresRepo:
    BASE_URI = f"http://localhost:{settings.API_PORT}"

    def __init__(self, ctx: Context) -> None:
        self.ctx = ctx

    async def fetch_all(self, user_id: int, rework_id: int) -> list[dict[str, Any]]:
        uri = f"{self.BASE_URI}/api/v1/reworks/{rework_id}/scores/{user_id}"
        resp = await self.ctx.http.get(uri)

        return resp.json()
