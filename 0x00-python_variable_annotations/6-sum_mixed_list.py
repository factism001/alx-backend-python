#!/usr/bin/env python3
"""Calculates the sum of a mixed int and float list.

This module provides a function to calculate the total sum of
a list containing integers and floats.
"""

from typing import List, Union

MixedList = List[Union[int, float]]


def sum_mixed_list(mxd_lst: MixedList) -> float:
    """Sums the values in a mixed int and float list.
    Args:
        mxd_lst (List[Union[int, float]]): The mixed list.

    Returns:
        float: The total sum of the list values as a float.
        """
    total = 0
    for num in mxd_lst:
        total += num
    return float(total)
