from __future__ import annotations

from typing import Any
from typing import Mapping

from pydantic import BaseModel


class Beatmap(BaseModel):
    id: int
    set_id: int
    song_name: str

    @classmethod
    def from_mapping(cls, mapping: Mapping[str, Any]) -> Beatmap:
        return cls(
            id=mapping["beatmap_id"],
            set_id=mapping["beatmapset_id"],
            song_name=mapping["song_name"],
        )
