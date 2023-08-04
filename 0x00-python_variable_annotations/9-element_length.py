#!/usr/bin/env python3
"""Annotate the function’s parameters and
return values with the appropriate types
"""

from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """
    Returns a list of tuples, each containing
    an element from the input list and its length.

    Args:
        lst (List[str]): The input list of strings.

    Returns:
        List[Tuple[str, int]]: A list of tuples where each tuple
        contains an element from the input list and its length.
    """
    return [(i, len(i)) for i in lst]
