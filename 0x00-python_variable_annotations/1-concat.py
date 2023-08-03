#!/usr/bin/env python3
"""Concatenates two strings together. 

This module provides a function for concatenating two string values 
and returning the concatenated string.
"""

from typing import TypeVar

String = TypeVar('String', str)

def concat(str1: String, str2: String) -> String:
    """Concatenates two strings together.
    
    Args:
        str1: The first string.
        str2: The second string.

    Returns:
        A string containing str1 + str2.
    """
    
    return str1 + str2
