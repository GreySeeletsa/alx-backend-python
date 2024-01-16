#!/usr/bin/env python3
"""module for task 0
"""


import asyncio
import random


async def async_generator():
    """Generates random numbers between 0 and 10, one number
    at a time.

    Yields:
        Generator[float, None, None]:  random num between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
