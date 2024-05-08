#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""
import csv
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Returns pagination information in a dictionary."""
        assert index is None or (isinstance(index, int) and index >= 0)
        assert isinstance(page_size, int) and page_size > 0

        dataset = self.dataset()
        total_rows = len(dataset)

        # Calculating the current index
        start_index = 0 if index is None else index * page_size

        # Calculating the next index
        next_index = min(start_index + page_size, total_rows)

        return {
            "index": start_index,
            "next_index": next_index if next_index < total_rows else None,
            "page_size": page_size,
            "data": dataset[start_index:next_index]
        }


server = Server()
