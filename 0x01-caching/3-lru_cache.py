#!/usr/bin/env python3
"""
Implementation of a LRU cache
"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache implements a simple LRU cache
    """
    def __init__(self):
        """ init function """
        super().__init__()
        self.lru = []

    def put(self, key, item):
        """ Adds the new item to the dictionary """
        if key is not None and item is not None:
            max_size = LRUCache.MAX_ITEMS
            self.cache_data[key] = item
            if key not in self.lru:
                self.lru.append(key)
            else:
                self.lru.pop(self.lru.index(key))
                self.lru.append(key)
        if len(self.cache_data) > max_size:
            discard_key = self.lru.pop(0)
            print("DISCARD:", discard_key)
            del self.cache_data[discard_key]

    def get(self, key):
        """ Returns the value of the key from the dictionary """
        if key is None:
            return None
        if key in self.cache_data.keys():
            self.lru.pop(self.lru.index(key))
            self.lru.append(key)
            return self.cache_data[key]
        return None
