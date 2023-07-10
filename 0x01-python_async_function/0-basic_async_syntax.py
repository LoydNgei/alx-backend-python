#!/usr/bin/env python3
"""Asynch coroutine"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Return random delay"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
