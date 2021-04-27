#!/usr/bin/env python3
"""
exercise module
"""
import redis
from functools import wraps
from typing import Union, Optional, Callable
from uuid import uuid4


def count_calls(method: Callable) -> Callable:
    """Count how many times methods of the Cache class are called"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """Increments the count for that key every
        time the method is called and returns the value
        returned by the original method"""
        self._redis.incr(key)
        return method(self, *args, **kwds)

    return wrapper


def call_history(method: Callable) -> Callable:
    """Creates input and output list keys, respectively"""
    @wraps(method)
    def wrapper(self, *args, **kwds):
        """Uses the decorated function’s qualified
        name and append ':inputs' and ':outputs'"""
        self._redis.rpush(method.__qualname__ + ":inputs", str(args))

        outputs = str(method(self, *args, **kwds))
        self._redis.rpush(method.__qualname__ + ":outputs", outputs)

        return outputs

    return wrapper


class Cache():
    """Cache class"""

    def __init__(self):
        """Constructor method"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Generates a random key, store the input data
        in Redis using the random key and return the key"""
        random_key = str(uuid4())
        self._redis.set(random_key, data)
        return random_key

    def get(self, key: str, fn: Optional[Callable] = None)\
            -> Union[str, bytes, int, float]:
        """Reads from Redis and recovers original type"""
        data = self._redis.get(key)
        if fn:
            data = fn(data)
        return data

    def get_str(self, data: bytes) -> str:
        """Converts bytes to string"""
        return data.decode("utf-8")

    def get_int(self, data: bytes) -> int:
        """Converts bytes to integer"""
        return int.from_bytes(date, byteorder)
