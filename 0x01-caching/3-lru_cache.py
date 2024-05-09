#!/usr/bin/env python3
"""
    Create a class LRUCache that inherits from BaseCaching
        Requirement:
            use self.cache_data
"""

from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """
    LRUCache class that inherits from BaseCaching
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

        if key in self.cache_data:
            del self.cache_data[key]

        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru_key, _ = self.cache_data.popitem(last=False)
            print("DISCARD:", lru_key)

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
