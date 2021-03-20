#!/usr/bin/python3
"""BasicCache"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache
    """

    def put(self, key, item):
        """Add an item in the cache
        """
        if None not in {key, item}:
            self.cache_data[key] = item

    def get(self, key):
        """Get an item by key
        """
        return self.cache_data.get(key, None)
