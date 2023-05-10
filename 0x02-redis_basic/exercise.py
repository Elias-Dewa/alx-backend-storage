#!/usr/bin/env python3
"""Writing strings to Redis"""

from typing import Union
from uuid import uuid4
import redis


class Cache():
    """Define a cache class
    """

    def __init__(self):
        """Initialize
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """method that generate a random key, store the input data in Redis
        using the random key

        Args:
            data (Union[str, bytes, int, float]): a data argument

        Returns:
            str: return the key
        """
        generate_random_key = str(uuid4())
        self._redis.set(generate_random_key, data)
        return generate_random_key
