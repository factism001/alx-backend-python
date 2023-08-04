#!/usr/bin/env python3
"""Adds two floats together.

This module provides a function to add two float values together
and return the result as a float.
"""

from typing import TypeVar Union

FloatNumber = TypeVar('FloatNumber', float, Union[float, int])


def add(a: FloatNumber, b: FloatNumber) -> FloatNumber:
    """Adds two float values together.

    Args:
        a: First float to add.
        b: Second float to add.

        Returns:
        The sum of a and b as a float.
    """

    return a + b
