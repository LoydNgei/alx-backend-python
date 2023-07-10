#!/usr/bin/env python3
"""Asynch coroutine"""
import random


async def wait_random(max_delay=10):
    delay = random.uniform(0, max_delay)
    return delay
