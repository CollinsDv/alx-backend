#!/usr/bin/env python3
"""
module 0-basic_cache
involves implementing the put and get method from base class

Create a class BasicCache that inherits from BaseCaching and is a caching system:

* You must use self.cache_data - dictionary from the parent class BaseCaching
* This caching system doesn’t have limit
* def put(self, key, item):
	* Must assign to the dictionary self.cache_data the item value for the key key.
	* If key or item is None, this method should not do anything.
* def get(self, key):
	* Must return the value in self.cache_data linked to key.
	* If key is None or if the key doesn’t exist in self.cache_data, return None.
"""
from typing import Any, Union
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """implements put and set operations for caching"""
    def __init__(self):
        super().__init__()

    def put(self, key: Any, item: Any) -> None:
        """adds item to cache
        Args:
            key (Any) -> key to a value
            item (Any) -> value associated to key
        """
        if key and item:
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
