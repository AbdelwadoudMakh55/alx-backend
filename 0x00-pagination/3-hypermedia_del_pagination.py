#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import Dict, List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Deletion-resilient hypermedia pagination
        """
        assert type(index) == int and index < len(self.dataset()) and index > 0
        assert type(page_size) == int and page_size > 0
        hyper_index = {}
        idx_dataset = self.indexed_dataset()
        try:
            if idx_dataset[index]:
                next_index = index + page_size
                data = [
                    idx_dataset[i] for i in range(index, index + page_size)
                ]
        except KeyError:
            next_index = list(idx_dataset.keys())[index + page_size]
            key = list(idx_dataset.keys())[index]
            data = [idx_dataset[i] for i in range(key, key + page_size)]
        hyper_index['index'] = index
        hyper_index['next_index'] = next_index
        hyper_index['page_size'] = page_size
        hyper_index['data'] = data
        return hyper_index
