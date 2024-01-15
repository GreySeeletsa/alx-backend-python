#!/usr/bin/env python3
"""Module for task 0
"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Waits for a random delay between 0 and
    max_delay seconds and eventually returns it

    Args:
        max_delay (int, optional): The maximum delay in seconds

    Returns:
        float: delay in seconds.
    """
    delay = random.random() * max_delay
    await asyncio.sleep(delay)
    return delay
