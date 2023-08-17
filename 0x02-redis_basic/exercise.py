#!/usr/bin/env python3
""" module creates class """


import uuid
import redis
from typing import Union, Callable


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

    def get(self, key: str, fn: Callable = None) -> Union[
            str, bytes, int, float, None]:
        """
            Retrieve data from the cache using the provided key.
            Args:
                key (str): The key associated with the data.
                fn (Callable, optional): A callable function to
                convert the data to a desired format.
            Returns:
                Union[str, bytes, int, float, None]:
                The retrieved data from the cache.
        """

        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> Union[str, None]:
        """
            Retrieve a string data from the cache using the provided key.
            Args:
                key (str): The key associated with the data.
            Returns:
                Union[str, None]: The retrieved string data from the cache.
        """

        return self.get(key, fn=lambda d: d.decode("utf-8") if d else None)

    def get_int(self, key: str) -> Union[int, None]:
        """
            Retrieve an integer data from the cache using the provided key.
            Args:
                key (str): The key associated with the data.
            Returns:
                Union[int, None]: The retrieved integer data from the cache.
        """

        return self.get(key, fn=int)
