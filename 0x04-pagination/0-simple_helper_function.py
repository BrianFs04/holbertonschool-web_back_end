#!/usr/bin/env python3
"""index_range"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters."""
    end_index = page * page_size
    start_index = (page - 1) * page_size
    res = (start_index, end_index)
    return res
