#!/usr/bin/env python3
"""Calculates the sum of a list of floats.

This module provides a function for finding the total sum of a
list containing float values.
"""

from typing import List

FloatNum = List[float]


def sum_list(input_list: FloatNum) -> float:
    """Calculates the sum of a list of floats.
    Args:
        input_list (List[float]): The list of floats to sum.

    Returns:
        float: The total sum of the float values in the list.
    """

    total = 0
    for num in input_list:
        total += num
    return total
