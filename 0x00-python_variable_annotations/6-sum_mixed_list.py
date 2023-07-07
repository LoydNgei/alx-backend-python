#!/usr/bin/env python3
"""Annonated func sum_mixed_list takes list mxd_lst"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns sum of the float"""
    return sum(mxd_lst)
