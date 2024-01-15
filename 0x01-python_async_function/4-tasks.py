#!/usr/bin/env python3
"""Module for task 4
"""


import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Take the code from wait_n and alter it into a new function


    Args:
        n (int): number of tasks to create


    Returns:
        List[float]: A list of asyncio.Task objects that asynchronously
        wait for random delays
    """
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
    )
    return sorted(wait_times)
