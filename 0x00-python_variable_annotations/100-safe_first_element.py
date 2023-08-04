#!/usr/bin/env python3
"""Augment the following code with
the correct duck-typed annotations
"""

from typing import Union


def safe_first_element(lst) -> Union[None, int, float, str, list, tuple, dict]:
    """
    Returns the first element of the input list or None if the list is empty.

    Args:
        lst: A list that can contain elements of any type.

    Returns:
        Union[None, int, float, str, list, tuple, dict, set]:
        The first element of the list or None if the list is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
