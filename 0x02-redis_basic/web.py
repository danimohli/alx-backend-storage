#!/usr/bin/env python3
"""
web
"""
import requests
import redis
from typing import Callable
from functools import wraps

# Redis connection
r = redis.Redis()


def track_url_access(method: Callable) -> Callable:
    """
    Decorator to track URL access count and cache HTML content.
    """
    @wraps(method)
    def wrapper(url: str) -> str:
        # Increment the access count for this URL
        count_key = f"count:{url}"
        r.incr(count_key)

        # Check if the page is cached
        cache_key = f"cache:{url}"
        cached_page = r.get(cache_key)

        if cached_page:
            # If cached, return the cached content
            return cached_page.decode('utf-8')

        # Otherwise, fetch the page and cache it for 10 seconds
        page = method(url)
        r.setex(cache_key, 10, page)
        return page

    return wrapper


@track_url_access
def get_page(url: str) -> str:
    """
    Fetches the HTML content of a given URL and returns it.
    """
    response = requests.get(url)
    return response.text
