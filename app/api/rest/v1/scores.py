from __future__ import annotations

from fastapi import APIRouter
from fastapi import Depends

from app.api.rest.context import RequestContext
from app.common import responses
from app.common.errors import ServiceError
from app.common.responses import Success
from app.models.score import Score
from app.usecases import scores

router = APIRouter()


@router.get("/v1/scores/{user_id}", response_model=Success[list[Score]])
async def get_scores(user_id: int, rework_id: int, ctx: RequestContext = Depends()):
    data = await scores.fetch_all(ctx, user_id, rework_id)
    if isinstance(data, ServiceError):
        return responses.failure(data, "Failed to fetch scores")

    return responses.success(data)
