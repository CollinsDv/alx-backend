#!/usr/bin/env python3
"""
module: 0-simple_helper_function

helps in determining the start and end index of a page
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    generate start and end index of a page
    Args:
        page (int) -> current page
        page_size (int) -> the size of the data to be fitted

    Returns:
        Tuple with start and end index values
    """
    start_index = (page - 1) * page_size
    end_index = page + page_size

    return (start_index, end_index)
