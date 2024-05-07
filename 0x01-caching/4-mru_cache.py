#!/usr/bin/env python3
"""
Implementation of a MRU cache
"""
import time
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache implements a simple MRU cache
    """
    def __init__(self):
        """ init function """
        super().__init__()
        self.mru = {}

    def put(self, key, item):
        """ Adds the new item to the dictionary """
        if key is not None and item is not None:
            max_size = MRUCache.MAX_ITEMS
            self.cache_data[key] = item
            self.mru[key] = time.time()
        if len(self.cache_data) > max_size:
            mru_time = 0
            discard_key = None
            for k, v in self.mru.items():
                if k != key and v > mru_time:
                    mru_time = v
                    discard_key = k
            print("DISCARD:", discard_key)
            del self.mru[discard_key]
            del self.cache_data[discard_key]

    def get(self, key):
        """ Returns the value of the key from the dictionary """
        if key is None:
            return None
        try:
            self.mru[key] = time.time()
            return self.cache_data[key]
        except KeyError:
            del self.mru[key]
            return None
