from __future__ import annotations

from fastapi.templating import Jinja2Templates

from app.api.filters import FILTERS
from app.api.filters import GLOBALS


templates = Jinja2Templates(directory="web/templates")
templates.env.globals |= GLOBALS
templates.env.filters |= FILTERS
