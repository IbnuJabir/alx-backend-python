#!/usr/bin/env python3
'''
    this module returns a value after a random delay
'''

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that takes in 2 int arguments (n and max_delay)
    and returns a list of delays
    """
    delays = []
    for _ in range(n):
        delays.append(wait_random(max_delay))
    return [await delay for delay in asyncio.as_completed(delays)]
