from __future__ import annotations

from typing import Any
from typing import Mapping
from typing import Optional

from pydantic import BaseModel


class LoginResponse(BaseModel):
    success: bool
    user_id: Optional[int]
    session_token: Optional[str]

    @classmethod
    def from_mapping(cls, mapping: Mapping[str, Any]) -> LoginResponse:
        return cls(
            success=mapping["success"],
            user_id=mapping["user_id"],
            session_token=mapping["session_token"],
        )


class QueueResponse(BaseModel):
    success: bool
    message: Optional[str]

    @classmethod
    def from_mapping(cls, mapping: Mapping[str, Any]) -> QueueResponse:
        return cls(
            success=mapping["success"],
            message=mapping.get("message"),
        )
