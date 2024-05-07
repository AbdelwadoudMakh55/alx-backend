#!/usr/bin/env python3
"""
Implementation of a FIFO cache
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    BaseCache implements a simple cache using a dictionary
    """
    def __init__(self):
        super().__init__()
        self.oldest = []

    def put(self, key, item):
        """ Adds the new item to the dictionary """
        if key is not None and item is not None:
            max_size = FIFOCache.MAX_ITEMS
            k_list = self.cache_data.keys()
            if len(self.cache_data) < max_size and key not in k_list:
                self.oldest.append(key)
            if key not in k_list and len(self.cache_data) == max_size:
                discarded_key = self.oldest.pop(0)
                self.oldest.append(key)
                del self.cache_data[discarded_key]
                print("DISCARDED:", discarded_key)
                self.cache_data[key] = item
            else:
                self.cache_data[key] = item

    def get(self, key):
        """ Returns the value of the key from the dictionary """
        if not key:
            return None
        try:
            return self.cache_data[key]
        except KeyError:
            return None
