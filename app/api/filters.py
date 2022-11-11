from __future__ import annotations

from typing import Union

import orjson
from fastapi import Request


def get_ctx_messages(request: Request) -> Union[list[dict[str, str]], list]:
    """Get messages from the request context"""

    try:
        errors = request.cookies["errors"]
        return orjson.loads(errors)
    except (KeyError, AttributeError):
        return []


def render_delta(old: int, new: int) -> str:

    delta = round(new - old, 2)

    if delta < 0:
        return f"""
        (+{abs(delta):,}
            <div class="inline-block before:content-['▲'] text-green-600"></div>
        )"""
    elif delta > 0:
        return f"""
        (-{abs(delta):,}
            <div class="inline-block before:content-['▼'] text-red-500"></div>
        )"""
    else:
        return f"""
        ({abs(delta):,}
            <div class="inline-block before:content-['▬'] text-gray-500"></div>
        )"""


def country_points(country: str) -> str:
    chars = []
    country = country.upper()

    for _chr in country:
        chars.append(format(ord(_chr) + 127397, "x"))

    return "-".join(chars)


def number_commas(number: int) -> str:
    return f"{number:,}"


GLOBALS = {
    "get_ctx_messages": get_ctx_messages,
}

FILTERS = {
    "render_delta": render_delta,
    "country": country_points,
    "number_commas": number_commas,
}
