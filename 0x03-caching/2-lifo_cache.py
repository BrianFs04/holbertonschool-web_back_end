#!/usr/bin/python3
"""LIFOCache module
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO caching"""

    def __init__(self):
        """Constructor method"""
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """Add an item in the cache
        """
        if None not in {key, item}:
            self.cache_data[key] = item
            if key not in self.keys:
                self.keys.append(key)
            else:
                self.keys.remove(key)
                self.keys.append(key)
            if(len(self.cache_data) > BaseCaching.MAX_ITEMS):
                last_key = self.keys.pop(-2)
                del self.cache_data[last_key]
                print("DISCARD: {}".format(last_key))

    def get(self, key):
        """Get an item by key
        """
        return self.cache_data.get(key, None)
