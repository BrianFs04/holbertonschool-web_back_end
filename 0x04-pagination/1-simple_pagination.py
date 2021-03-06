#!/usr/bin/env python3
"""
Simple pagination
"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters."""
    end_index = page * page_size
    start_index = (page - 1) * page_size
    res = (start_index, end_index)
    return res


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
        """Returns the appropriate page of the dataset
        """
        assert all(isinstance(i, int) for i in [page, page_size]) and all(
            i > 0 for i in [page, page_size])

        dataset = self.dataset()

        if dataset is not None:
            start, end = index_range(page, page_size)
            rows = dataset[start:end]
            return rows

        return []
