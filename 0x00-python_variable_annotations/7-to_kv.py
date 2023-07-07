#!/usr/bin/env python3
"""Annonated func to_kv.Takes str k and
an int or float as arguments
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple"""
    return k, float(v ** 2)
