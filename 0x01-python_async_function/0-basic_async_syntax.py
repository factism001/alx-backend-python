#!/usr/bin/env python3

"""
This module defines an asynchronous coroutine for generating a random delay.
"""

import asyncio
import random


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
