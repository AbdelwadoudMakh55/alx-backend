#!/usr/bin/env python3
"""
Implementation of a MRU cache
"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache implements a simple MRU cache
    """
    def __init__(self):
        """ init function """
        super().__init__()
        self.mru = []

    def put(self, key, item):
        """ Adds the new item to the dictionary """
        if key is not None and item is not None:
            max_size = MRUCache.MAX_ITEMS
            self.cache_data[key] = item
            if key not in self.mru:
                self.mru.append(key)
            else:
                self.mru.pop(self.mru.index(key))
                self.mru.append(key)
        if len(self.cache_data) > max_size:
            discard_key = self.mru.pop(-2)
            print("DISCARD:", discard_key)
            del self.cache_data[discard_key]

    def get(self, key):
        """ Returns the value of the key from the dictionary """
        if key is None:
            return None
        if key in self.mru:
            self.mru.pop(self.mru.index(key))
            self.mru.append(key)
            return self.cache_data[key]
        return None
