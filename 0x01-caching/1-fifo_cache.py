#!/usr/bin/env python3
"""
    Class FIFOCache that inherits
    from BaseCaching and is a caching system
        Requirement
            use self.cache_data dictionary
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """

    def __init__(self):
        """ Initialize
        """
        super().__init__()

    def put(self, key, value):
        """ Add an item in the cache
        """
        if key is not None and value is not None:
            if key in self.cache_data:
                del self.cache_data[key]
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded_key = next(iter(self.cache_data))
                print("DISCARD: {}".format(discarded_key))
                del self.cache_data[discarded_key]
            self.cache_data[key] = value

    def get(self, key):
        """ Get an item by key
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
