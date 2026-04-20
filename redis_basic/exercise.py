#!/usr/bin/env python3

from typing import Union
from uuid import uuid4


class Cache:
    """
    Cache class.
    """

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data and return a random key.
        """
        key = str(uuid4())
        return key