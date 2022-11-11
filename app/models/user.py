from __future__ import annotations

from typing import Any
from typing import Mapping

from pydantic import BaseModel

from app.models.rework import Rework


class User(BaseModel):
    id: int
    name: str
    country: str  # ISO
    reworks: list[Rework]

    @classmethod
    def from_mapping(cls, mapping: Mapping[str, Any]) -> User:
        return cls(
            id=mapping["user_id"],
            name=mapping["user_name"],
            country=mapping["country"],
            reworks=[Rework.from_mapping(rework) for rework in mapping["reworks"]],
        )


class UserQuery(BaseModel):
    id: int
    name: str

    @classmethod
    def from_mapping(cls, mapping: Mapping[str, Any]) -> UserQuery:
        return cls(
            id=mapping["user_id"],
            name=mapping["user_name"],
        )
