from __future__ import annotations

from fastapi import APIRouter

from . import homepage
from . import leaderboards
from . import sessions
from . import users


router = APIRouter()  # root page.

router.include_router(homepage.router, tags=["homepage"])
router.include_router(sessions.router, tags=["sessions"])
router.include_router(users.router, tags=["users"])
router.include_router(leaderboards.router, tags=["reworks"])
