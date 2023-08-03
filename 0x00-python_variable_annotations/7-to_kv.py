#!/usr/bin/env python3
"""Returns a tuple with a string and squared float value.

This module provides a function that takes a string and numeric value,
squares the numeric value, and returns them in a tuple pair.
"""

from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Creates a tuple from a string and numeric value.
    
    Args:
        k: The key string. 
        v: The numeric value to square.

    Returns:
        A tuple of the string k and float squared v.
    """

    v_squared = v ** 2
    return (k, float(v_squared))
