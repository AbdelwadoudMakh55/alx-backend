#!/usr/bin/env python3
"""
Module of hypermedia pagination
"""
import csv
import math
from typing import Dict, List


def index_range(page, page_size):
    """
    Function that calculates index range
    """
    return (page_size * (page - 1), page_size * page)


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
        """ Get page data
        """
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0
        start, end = index_range(page, page_size)
        if start > len(self.dataset()) - 1 or end > len(self.dataset()) - 1:
            return []
        return self.dataset()[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """ Get hypermedia
        """
        hypermedia = {}
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0
        data = self.get_page(page, page_size)
        start, end = index_range(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        hypermedia['page_size'] = len(data)
        hypermedia['page'] = page
        hypermedia['data'] = data
        hypermedia['next_page'] = None if len(data) == 0 else page + 1
        hypermedia['prev_page'] = None if page == 1 else page - 1
        hypermedia['total_pages'] = total_pages
        return hypermedia
