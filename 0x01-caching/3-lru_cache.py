#!/usr/bin/env python3
"""
Implementation of a LRU cache
"""
import math
import time
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache implements a simple LRU cache
    """
    def __init__(self):
        """ init function """
        super().__init__()
        self.lru = {}

    def put(self, key, item):
        """ Adds the new item to the dictionary """
        if key is not None and item is not None:
            max_size = LRUCache.MAX_ITEMS
            self.cache_data[key] = item
            self.lru[key] = time.time()
        if len(self.cache_data) > max_size:
            lru_time = math.inf
            discard_key = None
            for k, v in self.lru.items():
                if k != key and v < lru_time:
                    lru_time = v
                    discard_key = k
            print("DISCARD:", discard_key)
            del self.lru[discard_key]
            del self.cache_data[discard_key]

    def get(self, key):
        """ Returns the value of the key from the dictionary """
        if key is None:
            return None
        try:
            self.lru[key] = time.time()
            return self.cache_data[key]
        except KeyError:
            del self.lru[key]
            return None
