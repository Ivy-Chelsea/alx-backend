#!/usr/bin/env python3
"""
Simple helper function
"""


def index_range(page, page_size):
    """
    returns a tuple
    """
    if page and page_size:
        start_index = (page - 1) * page_size
        end_index = start_index + page_size
        return start_index, end_index
