#!/usr/bin/env python3
"""
module: 1-simple_pagination

helps in determining the start and end index of a page and
a class for reading and formatting output with hypermedia data
"""
from typing import List, Tuple
import csv
import math


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    generate start and end index of a page
    Args:
        page (int) -> current page
        page_size (int) -> the size of the data to be fitted

    Returns:
        Tuple with start and end index values
    """
    if isinstance(page, int) and isinstance(page_size, int) and\
            page > 0 and page_size > 0:
        start_index = (page - 1) * page_size
        end_index = page * page_size

        return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        returns a set of data within a particular range
        Args
            page (int) -> page number
            page_size (int) -> data size to embed in a page

        Returns
            List: list of names or empty list on error
        """
        assert isinstance(page, int) and page > 0, "Error: Page must be a \
                positive integer"
        assert isinstance(page_size, int) and page_size > 0, "Error: Page \
                size must be a positive integer"

        start_idx, last_idx = index_range(page, page_size)

        dataset = self.dataset()

        if start_idx >= len(dataset):
            return []

        return list(dataset[start_idx:last_idx])

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        returns a dict of hypermedia data within
        Args
            page (int) -> page number
            page_size (int) -> data size to embed in a page

        Returns
            dict of page hypermedia
        """
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        return {
                'page_size': len(data[0]),
                'page': page,
                'data': data,
                'next_page': page + 1 if page < total_pages else None,
                'prev_page': page - 1 if page > 1 else None,
                'total_pages': total_pages
                }
