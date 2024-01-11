#!/usr/bin/env python3
"""module for task 7
"""


from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Takes a str k and an int OR float v
    as arguments and returns a tuple

    Args:
        k (str): str to include in the tuple
        v (Union[int, float]): int or float to square and
        include in the tuple

    Returns:
        Tuple[str, float]: Tuple with the str as the 1st element
        and the squared int or float as the 2nd element
    """
    return (k, float(v**2))
