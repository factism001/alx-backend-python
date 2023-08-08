#!/usr/bin/env python3

"""
Asynchronous routine that spawns wait_random n times with specified max_delay.
"""

import asyncio
import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """
    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (float): The maximum delay in seconds.

    Returns:
        list[float]: List of delays in ascending order.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
