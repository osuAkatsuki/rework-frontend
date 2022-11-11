from __future__ import annotations

from typing import Any
from typing import Mapping

from pydantic import BaseModel


class Rework(BaseModel):
    id: int
    name: str
    mode: int
    relax: int
    updated_at: int

    @classmethod
    def from_mapping(cls, mapping: Mapping[str, Any]) -> Rework:
        return cls(
            id=mapping["rework_id"],
            name=mapping["rework_name"],
            mode=mapping["mode"],
            relax=mapping["rx"],
            updated_at=mapping["updated_at"],
        )
