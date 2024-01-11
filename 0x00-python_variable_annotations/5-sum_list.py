#!/usr/bin/env python3
"""module for task 5
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """Takes a list input_list of floats as
    argument and returns their sum as a float.

    Args:
        input_list (List[float]): list of floats

    Returns:
        float: Sum of elements in the list.
    """
    return float(sum(input_list))
