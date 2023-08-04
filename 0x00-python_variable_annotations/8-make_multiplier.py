#!/usr/bin/env python3
"""Returns a function that multiplies values by a multiplier."""

from typing import Callable

FloatNum = float


def make_multiplier(multiplier: FloatNum) -> Callable[[FloatNum], FloatNum]:
    """Creates a function that multiplies by a multiplier.
    Args:
        multiplier (float): The number to multiply by.

    Returns:
        A function that takes a float and returns
        the product with multiplier.
    """

    def multiplier_func(x: FloatNum) -> FloatNum:
        return multiplier * x

    return multiplier_func
