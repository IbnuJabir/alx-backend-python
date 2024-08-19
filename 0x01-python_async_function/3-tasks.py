#!/usr/bin/env python3
"""
This module contains the function for task 3.
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates and returns an asyncio.Task for the wait_random coroutine.

    Args:
        max_delay (int): The maximum delay for the wait_random coroutine.

    Returns:
        asyncio.Task: A Task object that represents the coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
