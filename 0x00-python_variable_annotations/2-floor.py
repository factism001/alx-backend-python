#!/usr/bin/env python3
"""Returns the floor of a float.

This module provides a function to calculate the floor of a 
provided float number.
"""

from typing import TypeVar
from math import floor as math_floor

FloatNum = TypeVar('FloatNum', float)

def floor(n: FloatNum) -> int:
    """Finds the floor of a float.
    
    Args:
       n(FloatNum): The float number to find floor of.
       
    Returns:
       int: The floor of n as an integer.
    """
    
    return math_floor(n)
