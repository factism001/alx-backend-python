#!/usr/bin/env python3

"""
This module defines functions using asyncio.Tasks.
"""

import asyncio
from typing import List
from asyncio.tasks import Task


async def wait_random(max_delay: float = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay.

    Args:
        max_delay (float): The maximum delay in seconds. Defaults to 10.

    Returns:
        float: The random delay that was waited.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


def task_wait_random(max_delay: int) -> Task:
    """
    Regular function that creates an asyncio.Task for wait_random.

    Args:
        max_delay (int): The maximum delay in seconds.

    Returns:
        asyncio.Task: An asyncio.Task instance for wait_random.
    """
    loop = asyncio.get_event_loop()
    return loop.create_task(wait_random(max_delay))


async def task_wait_n(n: int, max_delay: float) -> List[float]:
    """
    Asynchronous function that creates and awaits asyncio.Tasks.

    Args:
        n (int): The number of tasks to create.
        max_delay (float): The maximum delay in seconds.

    Returns:
        List[float]: List of delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
