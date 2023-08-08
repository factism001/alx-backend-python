#!/usr/bin/env python3
"""
This module defines a function that measures total execution time for wait_n.
"""
import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures total execution time for wait_n(n, max_delay).

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (float): The maximum delay in seconds.

    Returns:
        float: Total time for execution wait_n(n, max_delay).
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()
    total_time = end - start
    return total_time / n
