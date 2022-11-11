from __future__ import annotations

from fastapi import APIRouter
from fastapi import Depends

from app.api.rest.context import RequestContext
from app.common import responses
from app.common.errors import ServiceError
from app.common.responses import Success
from app.models.stats import UserStats
from app.usecases import stats

router = APIRouter()


@router.get("/v1/stats/{user_id}", response_model=Success[UserStats])
async def get_stats(user_id: int, rework_id: int, ctx: RequestContext = Depends()):
    data = await stats.fetch_one(ctx, user_id, rework_id)
    if isinstance(data, ServiceError):
        return responses.failure(data, "Failed to fetch stats")

    return responses.success(data)
