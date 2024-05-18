#!/usr/bin/env python3
"""
    get_hyper method that take the same method as get_page
"""

import csv
from typing import List, Dict, Any
import math


def index_range(page: int, page_size: int) -> tuple:
    """
    Returns a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing the start index and end index.
    """
    first_index = (page - 1) * page_size
    last_index = page * page_size
    return first_index, last_index


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
        """Get a page from the dataset.

        Args:
            page (int): The current page number (default is 1).
            page_size (int): The number of items per page (default is 10).

        Returns:
            List[List]: The list of rows for the specified page.
        """
        # page and page_size are positive integers
        assert isinstance(page, int) and page > 0, "positive integer"
        assert isinstance(page_size, int) and page_size > 0, "positive integer"

        start_index, end_index = index_range(page, page_size)

        dataset = self.dataset()

        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """Get a page from the dataset with additional pagination info.

        Args:
            page (int): The current page number (default is 1).
            page_size (int): The number of items per page (default is 10).

        Returns:
            Dict[str, Any]: A dictionary containing pagination details.
        """
        data = self.get_page(page, page_size)
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)

        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
