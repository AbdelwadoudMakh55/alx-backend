#!/usr/bin/env python3
"""
Implementation of a LIFO cache
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache implements a simple LIFO cache
    """
    def __init__(self):
        """ init function """
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """ Adds the new item to the dictionary """
        if key is not None and item is not None:
            max_size = LIFOCache.MAX_ITEMS
            k_list = self.cache_data.keys()
            if key not in k_list:
                self.stack.append(key)
            self.cache_data[key] = item
            if len(self.cache_data) > max_size:
                discarded_key = self.stack.pop(-2)
                del self.cache_data[discarded_key]
                print("DISCARD:", discarded_key)

    def get(self, key):
        """ Returns the value of the key from the dictionary """
        if key is None:
            return None
        try:
            return self.cache_data[key]
        except KeyError:
            return None
