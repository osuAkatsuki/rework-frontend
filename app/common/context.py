from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from app.services import http


class Context(ABC):
    @property
    @abstractmethod
    def http(self) -> http.ServiceHTTP:
        ...
