#!/usr/bin/env python3
"""
Implementation of a LFU cache
"""
import math
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache implements a simple LFU cache
    """
    def __init__(self):
        """ init function """
        super().__init__()
        self.lfu = {}
        self.lru = []

    def put(self, key, item):
        """ Adds the new item to the dictionary """
        if key is not None and item is not None:
            max_size = LFUCache.MAX_ITEMS
            self.cache_data[key] = item
            if key not in self.lru:
                self.lfu[key] = 1
                self.lru.append(key)
            else:
                self.lfu[key] += 1
                self.lru.pop(self.lru.index(key))
                self.lru.append(key)
        if len(self.cache_data) > max_size:
            lfu = []
            lfu_n = math.inf
            for k, v in self.lfu.items():
                if k != key:
                    if v < lfu_n:
                        lfu.clear()
                        lfu.append(k)
                        lfu_n = v
                    elif v == lfu_n:
                        lfu.append(k)
            if len(lfu) == 1:
                discard_key = lfu[0]
            else:
                discard_key = None
                for key in lfu:
                    for k in self.lru:
                        if key == k:
                            discard_key = key
                            break
                    if discard_key is not None:
                        break
            print("DISCARD:", discard_key)
            del self.lfu[discard_key]
            del self.cache_data[discard_key]

    def get(self, key):
        """ Returns the value of the key from the dictionary """
        if key is None:
            return None
        if key in self.cache_data.keys():
            self.lfu[key] += 1
            self.lru.pop(self.lru.index(key))
            self.lru.append(key)
            return self.cache_data[key]
        return None
