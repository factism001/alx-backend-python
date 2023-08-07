#!/usr/bin/env python3

"""
This module defines a regular function for creating an asyncio.Task.
"""

import asyncio
from asyncio.tasks import Task
from 0-basic_async_syntax import wait_random


def task_wait_random(max_delay: int) -> Task:
    """
    Regular function that creates an asyncio.Task for wait_random.

    Args:
        max_delay (int): The maximum delay in seconds.

    Returns:
        asyncio.Task: An asyncio.Task instance for wait_random.
    """

    loop = asyncio.get_event_loop()
    task = loop.create_task(wait_random(max_delay))
    return task
