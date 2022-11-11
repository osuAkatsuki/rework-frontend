from __future__ import annotations

from fastapi import APIRouter

from . import leaderboards
from . import reworks
from . import scores
from . import sessions
from . import stats
from . import users


router = APIRouter(prefix="/api")

router.include_router(leaderboards.router, tags=["leaderboards"])
router.include_router(reworks.router, tags=["reworks"])
router.include_router(scores.router, tags=["scores"])
router.include_router(sessions.router, tags=["sessions"])
router.include_router(stats.router, tags=["stats"])
router.include_router(users.router, tags=["users"])
