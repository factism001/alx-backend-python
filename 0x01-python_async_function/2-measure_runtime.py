#!/usr/bin/env python3
"""
This module defines a function that measures total execution time for wait_n.
"""
from asyncio import run
from time import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures total execution time for wait_n(n, max_delay).

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay in seconds.

    Returns:
        float: Total time for execution wait_n(n, max_delay).
    """
    start = time()

    run(wait_n(n, max_delay))

    end = time()

    return (end - start) / n
