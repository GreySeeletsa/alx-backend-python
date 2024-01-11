#!/usr/bin/env python3
"""module for task 8
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Takes a float multiplier as argument
    and returns a function that multiplies a float by multiplier

    Args:
        multiplier (float): To use as the multiplier

    Returns:
        Callable[[float], float]: func that multiplies a float by
        the multiplier
    """
    return lambda x: x * multiplier
