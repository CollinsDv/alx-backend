#!/usr/bin/env python3
"""
module 1-fifo_cache
Create a class FIFOCache that inherits from BaseCaching
and is a caching system:

    You must use self.cache_data - dictionary from the
    parent class BaseCaching
    You can overload def __init__(self): but don’t forget
    to call the parent init: super().__init__()
    def put(self, key, item):
      - Must assign to the dictionary self.cache_data the item
      value for the key key.
      - If key or item is None, this method should not do anything.
      - If the number of items in self.cache_data is higher that
        BaseCaching.MAX_ITEMS:
        - you must discard the first item put in cache (FIFO algorithm)
        - you must print DISCARD: with the key discarded and following
          by a new line
    def get(self, key):
      - Must return the value in self.cache_data linked to key.
      - If key is None or if the key doesn’t exist in self.cache_data,
        return None.
"""
from typing import Any, Union
from collections import deque
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """implements FIFO caching algorithm
    Args:
        BaseCaching (class) -> Parent class
    """
    def __init__(self):
        super().__init__()
        self.queue = deque()

    def put(self, key: Any, item: Any) -> None:
        """adds item to cache
        Args:
            key (Any) -> key to a value
            item (Any) -> value associated to key
        """
        if key and item:
            if len(self.cache_data) < type(self).MAX_ITEMS:
                # add item to cache and queue
                self.queue.append(key)
                self.cache_data[key] = item
            else:
                # check for cache misses
                if key not in self.queue:
                    key_to_remove = self.queue.popleft()
                    print(f'DISCARD: {key_to_remove}')
                    del self.cache_data[key_to_remove]

                    # update cache and queue
                    self.queue.append(key)
                    self.cache_data[key] = item
                else:
                    # handle cache hit
                    if self.cache_data[key] is not item:
                        self.cache_data[key] = item

    def get(self, key: Any) -> Union[Any, None]:
        """get a value in cache
        Args:
            key: key to associative value
        Returns
            value of a key, else None
        """
        if key and key in self.cache_data:
            return self.cache_data[key]
        return None
