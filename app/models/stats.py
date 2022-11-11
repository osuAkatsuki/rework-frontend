from __future__ import annotations

from typing import Any
from typing import Mapping

from pydantic import BaseModel

# tsunyoku is lazy.
class UserStats(BaseModel):
    user_id: int
    country: str
    user_name: str
    new_pp: int
    old_pp: int
    new_rank: int
    old_rank: int

    @classmethod
    def from_mapping(cls, mapping: Mapping[str, Any]) -> UserStats:
        return cls(
            user_id=mapping["user_id"],
            country=mapping["country"],
            user_name=mapping["user_name"],
            new_pp=mapping["new_pp"],
            old_pp=mapping["old_pp"],
            new_rank=mapping["new_rank"],
            old_rank=mapping["old_rank"],
        )
