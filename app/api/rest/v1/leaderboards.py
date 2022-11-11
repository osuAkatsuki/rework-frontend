from __future__ import annotations

from fastapi import APIRouter
from fastapi import Depends

from app.api.rest.context import RequestContext
from app.common import responses
from app.common.errors import ServiceError
from app.common.responses import Success
from app.models.leaderboard import Leaderboard
from app.usecases import leaderboards

router = APIRouter()


@router.get("/v1/leaderboards/{rework_id}", response_model=Success[Leaderboard])
async def get_leaderboard(
    rework_id: int,
    page: int,
    limit: int,
    ctx: RequestContext = Depends(),
):
    data = await leaderboards.fetch_one(ctx, rework_id, page, limit)
    if isinstance(data, ServiceError):
        return responses.failure(data, "Failed to fetch leaderboard")

    return responses.success(data)
