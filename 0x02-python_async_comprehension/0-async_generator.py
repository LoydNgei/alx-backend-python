#!/usr/bin/env python3
"""Async generator function """
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Return random no btwn 0 and 10"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)