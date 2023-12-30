from __future__ import annotations

from typing import Any
from typing import Optional

from app.common import settings
from app.common.context import Context


class SessionsRepo:
    BASE_URI = settings.PERFORMANCE_SERVICE_BASE_URL

    def __init__(self, ctx: Context) -> None:
        self.ctx = ctx

    async def create(self, username: str, password_md5: str) -> dict[str, Any]:
        uri = f"{self.BASE_URI}/api/v1/reworks/sessions"
        resp = await self.ctx.http.post(
            uri,
            json={
                "username": username,
                "password_md5": password_md5,
            },
        )
        return resp.json()

    async def delete(self, uuid_token: str) -> None:
        uri = f"{self.BASE_URI}/api/v1/reworks/sessions/{uuid_token}"
        await self.ctx.http.delete(uri)

    async def enqueue(
        self,
        rework_id: int,
        uuid_token: str,
    ) -> Optional[dict[str, Any]]:
        uri = f"{self.BASE_URI}/api/v1/reworks/{rework_id}/queue"
        resp = await self.ctx.http.post(
            uri,
            params={"session": uuid_token},
        )

        if resp.status_code not in range(200, 300):
            return None

        return resp.json()
