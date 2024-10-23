#!/usr/bin/env python3
"""
Python Exercise for redis
"""
import redis
import uuid
from functools import wraps
from typing import Callable, Union, Optional


def count_calls(method: Callable) -> Callable:
    """
    A decorator that counts the number of times a method is called.

    Args:
        method (Callable): The method to be wrapped.

    Returns:
        Callable: The wrapped method with call count functionality.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Increment the call count in Redis each time the method is called.
        """
        key = f"{method.__qualname__}"
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


class Cache:
    """
    Class Cache for python impl of redis
    """
    def __init__(self):
        """
        Initialize Redis client and flush the database
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the given data in Redis with a random key and return the key.

        Args:
            data (Union[str, bytes, int, float]): The data to store.

        Returns:
            str: The key under which the data was stored.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Optional[Union[str, bytes, int, float]]:
        """
        Retrieve the value from Redis and apply an optional
        callable to convert it to the desired type.

        Args:
            key (str): The Redis key.
            fn (Optional[Callable]): A callable function to apply on
            the retrieved data for conversion.

        Returns:
            Optional[Union[str, bytes, int, float]]: The value from Redis,
            converted by fn if provided, or None if the key does not exist.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve a string value from Redis by
        automatically converting bytes to a string.

        Args:
            key (str): The Redis key.

        Returns:
            Optional[str]: The value as a string, or
            None if the key does not exist.
        """
        return self.get(key, lambda data: data.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve an integer value from Redis by
        automatically converting bytes to an integer.

        Args:
            key (str): The Redis key.

        Returns:
            Optional[int]: The value as an integer, or
            None if the key does not exist.
        """
        return self.get(key, lambda data: int(data))
