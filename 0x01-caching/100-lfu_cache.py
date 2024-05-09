#!/usr/bin/env python3
"""
    Write a class LFUCache that inherits from BaseCaching
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache class that inherits from BaseCaching
    """

    def __init__(self):
        """
        Constructor to initialize the cache
        """
        super().__init__()
        self.cache_data = {}
        self.frequency = {}
        self.access_time = {}
        self.time = 0

    def put(self, key, item):
        """
        Add or update an item in the cache
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            del self.cache_data[key]

        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Define the key function
            lfu_key = min(self.frequency, key=lambda k: (self.frequency[k], self.access_time[k]))
            del self.cache_data[lfu_key]
            del self.frequency[lfu_key]
            del self.access_time[lfu_key]
            print("DISCARD:", lfu_key)

        self.cache_data[key] = item
        self.frequency[key] = self.frequency.get(key, 0) + 1
        self.access_time[key] = self.time
        self.time += 1

    def get(self, key):
        """
        Retrieve an item from the cache
        """
        if key is None or key not in self.cache_data:
            return None

        item = self.cache_data.pop(key)
        self.cache_data[key] = item
        self.frequency[key] = self.frequency.get(key, 0) + 1
        self.access_time[key] = self.time
        self.time += 1
        return item
