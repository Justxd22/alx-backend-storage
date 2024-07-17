#!/usr/bin/env python3
"""Simplee result cache."""


import requests
import redis
from typing import Any, Callable
from functools import wraps

db = redis.Redis()


def cacheR(method: Callable) -> Callable:
    """Simplee result cache."""
    @wraps(method)
    def invoker(url) -> str:
        db.incr(f'count:{url}')
        data = db.get(f'result:{url}')
        if data:
            return data.decode('utf-8')
        data = method(url)
        db.set(f'count:{url}', 0)
        db.setex(f'result:{url}', 10, data)
        return data
    return invoker


@cacheR
def get_page(url: str) -> str:
    """Simplee result cache."""
    return requests.get(url).text
