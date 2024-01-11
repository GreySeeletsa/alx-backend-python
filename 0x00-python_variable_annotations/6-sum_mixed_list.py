#!/usr/bin/env python3
"""module for task 6
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Takes a list mxd_lst of integers
    and floats and returns their sum as a float.

    Args:
        mxd_lst (List[Union[int, float]]): list of integers and
        floats to sum.

    Returns:
        float: Sum of elements in the list.
    """
    return float(sum(mxd_lst))
