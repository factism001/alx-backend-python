#!/usr/bin/env python3 
"""Converts a float to a string.

This module provides a function to convert a float
number to its string representation.
"""

from typing import TypeVar

FloatNum = TypeVar('FloatNum', float)

def to_str(n: FloatNum) -> str:
    """Converts a float to a string.
    
    Args:
       n(FloatNum): The float to convert.
    
    Returns:
        str: The string representation of the float.
    """

    return str(n)
