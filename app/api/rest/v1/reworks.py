from __future__ import annotations

from fastapi import APIRouter
from fastapi import Depends

from app.api.rest.context import RequestContext
from app.common import responses
from app.common.errors import ServiceError
from app.common.responses import Success
from app.models.rework import Rework
from app.usecases import reworks

router = APIRouter()


@router.get("/v1/reworks", response_model=Success[list[Rework]])
async def get_reworks(ctx: RequestContext = Depends()):
    data = await reworks.fetch_all(ctx)
    if isinstance(data, ServiceError):
        return responses.failure(data, "Failed to get reworks")

    return responses.success(data)


@router.get("/v1/reworks/{rework_id}", response_model=Success[Rework])
async def get_rework(rework_id: int, ctx: RequestContext = Depends()):
    data = await reworks.fetch_one(ctx, rework_id)
    if isinstance(data, ServiceError):
        return responses.failure(data, "Failed to get rework")

    return responses.success(data)
