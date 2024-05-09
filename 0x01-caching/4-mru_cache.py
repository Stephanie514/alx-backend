#!/usr/bin/env python3
"""
    Create a class MRUCache that inherits from BaseCaching
"""

from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """
    MRUCache class that inherits from BaseCaching
    """

    def __init__(self):
        """
        Constructor to initialize the cache
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, value):
        """
        Add or update an item in the cache
        """
        if key is None or value is None:
            return

        # If the key already exists, remove it to update the order
        if key in self.cache_data:
            del self.cache_data[key]

        # If the cache is full, discard the most recently used item
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            mru_key = next(reversed(self.cache_data))
            print("DISCARD:", mru_key)
            del self.cache_data[mru_key]

        self.cache_data[key] = value

    def get(self, key):
        """
        Retrieve an item from the cache
        """
        if key is None or key not in self.cache_data:
            return None

        value = self.cache_data.pop(key)
        self.cache_data[key] = value
        return value
