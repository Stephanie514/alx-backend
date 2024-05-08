#!/usr/bin/env python3
"""
function named index_range
"""
import csv
from typing import List
from math import ceil


def index_range(page: int, page_size: int) -> tuple:
    """
    Returns a tuple of size two containing a
    start index and an end index corresponding
    to the range of indexes to return in a list
    for those particular pagination parameters
    """
    return ((page - 1) * page_size, page * page_size)


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__baby_data = None

    def baby_data(self) -> List[List]:
        """Cached baby data"""
        if self.__baby_data is None:
            with open(self.DATA_FILE) as file:
                reader = csv.reader(file)
                data = [row for row in reader]
            self.__baby_data = data[1:]

        return self.__baby_data

    def get_page(self,
                 page_num: int = 1,
                 size_of_page: int = 10) -> List[List]:
        """Returns the appropriate page of
        the dataset based on page_num and size_of_page."""
        assert isinstance(page_num, int) and page_num > 0
        assert isinstance(size_of_page, int) and size_of_page > 0

        start_index, end_index = index_range(page_num, size_of_page)
        baby_data = self.baby_data()
        if start_index >= len(baby_data):
            return []
        return baby_data[start_index:end_index]


server = Server()
