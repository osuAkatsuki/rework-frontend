from __future__ import annotations

from typing import Any
from typing import Mapping

from pydantic import BaseModel

from app.models.stats import UserStats


class Leaderboard(BaseModel):
    total_count: int
    users: list[UserStats]

    @classmethod
    def from_mapping(cls, mapping: Mapping[str, Any]) -> Leaderboard:
        return cls(
            total_count=mapping["total_count"],
            users=[UserStats.from_mapping(user) for user in mapping["users"]],
        )
