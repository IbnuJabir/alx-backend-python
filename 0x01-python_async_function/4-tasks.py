#!/usr/bin/env python3
'''
    this module contains the function for task 4
'''

import asyncio

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> asyncio.Task:
    """
    Asynchronous coroutine that takes in 2 int arguments (n and max_delay)
    and returns a list of delays
    """
    delays = []
    for _ in range(n):
        delays.append(task_wait_random(max_delay))
    return [await delay for delay in asyncio.as_completed(delays)]
