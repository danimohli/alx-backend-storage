#!/usr/bin/env python3
"""
Redis and Python interaction
"""

import uuid
from functools import wraps
from typing import Callable, Union
import redis


def track_calls(method: Callable) -> Callable:
    """
    Decorator that tracks the number of times a method is called.

    Args:
        method (Callable): Method to be wrapped.

    Returns:
        Callable: Wrapped method that increments the call count.
    """
    method_key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Increments the call count for the method every time it is called
        and returns the value returned by the original method.
        """
        self._redis.incr(method_key)
        return method(self, *args, **kwargs)
    return wrapper


def log_history(method: Callable) -> Callable:
    """
    Decorator to store the input and output history for a method.

    Args:
        method (Callable): Method to be wrapped.

    Returns:
        Callable: Wrapped method that logs its input and output.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Logs the input and output of each method call in Redis.
        """
        input_log_key = method.__qualname__ + ":inputs"
        output_log_key = method.__qualname__ + ":outputs"

        result = method(self, *args, **kwargs)

        self._redis.rpush(input_log_key, str(args))
        self._redis.rpush(output_log_key, str(result))

        return result

    return wrapper


def display_history(fn: Callable):
    """
    Displays the call history of a method.

    Args:
        fn (Callable): The function whose call history is displayed.
    """
    redis_instance = redis.Redis()
    method_name = fn.__qualname__
    call_count = redis_instance.get(method_name)
    try:
        call_count = call_count.decode('utf-8')
    except Exception:
        call_count = 0
    print(f'{method_name} was called {call_count} times:')

    inputs = redis_instance.lrange(method_name + ":inputs", 0, -1)
    outputs = redis_instance.lrange(method_name + ":outputs", 0, -1)

    for input_data, output_data in zip(inputs, outputs):
        try:
            input_data = input_data.decode('utf-8')
        except Exception:
            input_data = ""
        try:
            output_data = output_data.decode('utf-8')
        except Exception:
            output_data = ""

        print(f'{method_name}(*{input_data}) -> {output_data}')


class Cache():
    """
    Cache class for interacting with Redis.
    """

    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    @track_calls
    @log_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores data in Redis with a generated key.

        Args:
            data (Union[str, bytes, int, float]): The data to store.

        Returns:
            str: The key under which the data is stored.
        """
        unique_key = str(uuid.uuid4())
        self._redis.set(unique_key, data)
        return unique_key

    def retrieve(self, key: str, transform_fn: Callable = None)\
            -> Union[str, bytes, int, float]:
        """
        Retrieves data from Redis and applies a transformation if provided.

        Args:
            key (str): The key of the stored data.
            transform_fn (Callable, optional): A function to transform the data
            Defaults to None.

        Returns:
            Union[str, bytes, int, float]: The retrieved and possibly
            transformed data
        """
        data = self._redis.get(key)
        if transform_fn:
            return transform_fn(data)
        return data

    def retrieve_as_str(self, key: str) -> str:
        """
        Converts Redis-stored data to a string.

        Args:
            key (str): The key of the stored data.

        Returns:
            str: The data as a UTF-8 string.
        """
        stored_data = self._redis.get(key)
        return stored_data.decode("UTF-8")

    def retrieve_as_int(self, key: str) -> int:
        """
        Converts Redis-stored data to an integer.

        Args:
            key (str): The key of the stored data.

        Returns:
            int: The data as an integer, or 0 if conversion fails.
        """
        stored_data = self._redis.get(key)
        try:
            return int(stored_data.decode("UTF-8"))
        except Exception:
            return 0
