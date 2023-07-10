#!/usr/bin/env python3
"""Takes an int and return asyncio Task"""
import asyncio
from asyncio import Task
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """Returns a asyncio Task"""
    return asyncio.create_task(wait_random(max_delay))
