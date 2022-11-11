from __future__ import annotations

from enum import Enum


class ServiceError(str, Enum):
    SESSIONS_INVALID_CREDENTIALS = "sessions.invalid_credentials"
    USERS_NOT_FOUND = "users.not_found"
    SESSION_ENQUEUE_FAILED = "session.enqueue_failed"
    LEADERBOARDS_NOT_FOUND = "leaderboards.not_found"
    REWORKS_NOT_FOUND = "reworks.not_found"
    SCORES_NOT_FOUND = "scores.not_found"
    STATS_NOT_FOUND = "stats.not_found"
