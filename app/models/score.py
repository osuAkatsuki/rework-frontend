from __future__ import annotations

from typing import Any
from typing import Mapping

from pydantic import BaseModel

from app.models.beatmap import Beatmap


class Score(BaseModel):
    id: int
    user_id: int
    rework_id: int
    score: int
    mods: int
    max_combo: int
    accuracy: float
    n300: int
    n100: int
    n50: int
    ngeki: int
    nkatu: int
    nmiss: int
    old_pp: float
    new_pp: float
    old_rank: int
    new_rank: int
    beatmap: Beatmap

    @classmethod
    def from_mapping(cls, mapping: Mapping[str, Any]) -> Score:
        return cls(
            id=mapping["score_id"],
            user_id=mapping["user_id"],
            rework_id=mapping["rework_id"],
            score=mapping["score"],
            mods=mapping["mods"],
            max_combo=mapping["max_combo"],
            accuracy=mapping["accuracy"],
            n300=mapping["num_300s"],
            n100=mapping["num_100s"],
            n50=mapping["num_50s"],
            ngeki=mapping["num_gekis"],
            nkatu=mapping["num_katus"],
            nmiss=mapping["num_misses"],
            old_pp=mapping["old_pp"],
            new_pp=mapping["new_pp"],
            old_rank=mapping["old_rank"],
            new_rank=mapping["new_rank"],
            beatmap=Beatmap.from_mapping(mapping["beatmap"]),
        )
