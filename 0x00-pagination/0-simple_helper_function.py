#!/usr/bin/env python3
"""
Module of the helper function
"""


def index_range(page, page_size):
    """
    Function that calculates index range
    """
    return (page_size * (page - 1), page_size * page)
