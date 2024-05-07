#!/usr/bin/env python3
"""
Implementation of a basic cache system
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    BaseCache implements a simple cache using a dictionary
    """

    def put(self, key, item):
        """ Adds the new item to the dictionary """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Returns the value of the key from the dictionary """
        if not key:
            return None
        try:
            return self.cache_data[key]
        except KeyError:
            return None
