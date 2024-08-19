#!/usr/bin/env python3
# 0-basic_async_syntax.py
'''
    The basics of async.
'''

import asyncio
import random
from typing import Union


async def wait_random(max_delay: Union[int, float] = 10) -> float:
    """
    waits for a random delay between 0 and max_delay (included and float value)
    seconds and eventually returns it.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
