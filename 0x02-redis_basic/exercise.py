#!/usr/bin/env python3

from typing import Callable, Optional, Union
from uuid import uuid4
import redis
from functools import wraps

"""
Writing strings to Redis.
"""

def count_calls(method: Callable) -> Callable:
    """
    Counts the number of times a method is called.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper function to increment call count and run method.
        """
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    
    return wrapper

def call_history(method: Callable) -> Callable:
    """
    Decorator to store the history of inputs and
    outputs for a particular function.
    """
    key = method.__qualname__
    inputs = key + ":inputs"
    outputs = key + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper to record input/output history
        """
        self._redis.rpush(inputs, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(outputs, str(result))
        return result
    
    return wrapper


def replay(method: Callable) -> None:
    """
    Replays the history of a function.
    Args:
        method: The function whose call history we want to display.
    Returns:
        None
    """

    key = method.__qualname__
    

    cache = redis.Redis()

    call_count = cache.get(key)
    if call_count:
        call_count = int(call_count.decode("utf-8"))
    else:
        call_count = 0

    print(f"{key} was called {call_count} times:")


    inputs = cache.lrange(f"{key}:inputs", 0, -1)
    outputs = cache.lrange(f"{key}:outputs", 0, -1)

    for inp, outp in zip(inputs, outputs):
        inp = inp.decode("utf-8")
        outp = outp.decode("utf-8")
        print(f"{key}(*{inp}) -> {outp}")

class Cache:
    """
    Cache class to interact with Redis.
    """
    def __init__(self):
        """
        Initialize Redis client and flush datab
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis with a random key.
        """
        random_key = str(uuid4())
        self._redis.set(random_key, data)
        return random_key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """
        Retrieve data from Redis.
        """
        value = self._redis.get(key)
        if fn:
            value = fn(value)
        return value

    def get_str(self, key: str) -> str:
        """
        Retrieve data from Redis as a string.
        """
        value = self._redis.get(key)
        return value.decode('utf-8')

    def get_int(self, key: str) -> int:
        """
        Retrieve data from Redis as an integer.
        """
        value = self._redis.get(key)
        try:
            return int(value.decode('utf-8'))
        except Exception:
            return 0
