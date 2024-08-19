#!/usr/bin/env python3
# 0-basic_async_syntax.py

'''
This module contains a coroutine that waits for a random delay
between 0 and max_delay seconds and returns the delay.
'''

import asyncio
import random
from typing import Union


async def wait_random(max_delay: Union[int, float] = 10) -> float:
    """
    Waits for a random delay between 0 and max_delay seconds.

    Args:
        max_delay (int/float): The maximum delay in seconds. Defaults to 10.

    Returns:
        float: The actual delay that was waited.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
