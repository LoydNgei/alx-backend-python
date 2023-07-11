#!/usr/bin/env python3
"""Async coprehensions """
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Return 10 random numbers"""
    outcome = [i async for i in async_generator()]
    return outcome
