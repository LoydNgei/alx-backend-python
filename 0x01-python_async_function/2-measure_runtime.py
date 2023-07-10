#!/usr/bin/env python3
"""Measure the runtime"""
import time
from asyncio import run
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Return the runtime"""
    begin_time = time.time()
    run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - begin_time
    return total_time / n
