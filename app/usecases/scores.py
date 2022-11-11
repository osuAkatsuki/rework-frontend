from __future__ import annotations

from typing import Union

from app.common.context import Context
from app.common.errors import ServiceError
from app.models.score import Score
from app.repositories.scores import ScoresRepo


async def fetch_all(
    ctx: Context,
    user_id: int,
    rework_id: int,
) -> Union[list[Score], ServiceError]:
    s_repo = ScoresRepo(ctx)
    resp = await s_repo.fetch_all(user_id, rework_id)

    if not resp:
        return ServiceError.SCORES_NOT_FOUND

    return [Score.from_mapping(score) for score in resp]
