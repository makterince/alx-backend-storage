#!/usr/bin/env python3
""" module creates class """


import uuid
import redis
from typing import Union


class Cache:
    """ A cache class that uses Redis to store data with randm keys """

    def __init__(self):
        """ initialize the Cache instance and set up the Redis client """

        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
            Store the provided data in Redis with a randomly generated key.
            Args:
                data (Union[str, bytes, int, float]): The data to
                be stored in the cache.
            Returns:
                str: The randomly generated key used to store the data
                in the cache
        """

        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
