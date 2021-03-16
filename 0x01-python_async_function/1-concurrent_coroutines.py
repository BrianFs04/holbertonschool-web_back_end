#!/usr/bin/env python3
"""wait_n"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Multiple coroutines at the same time with async
    """
    delays, sort_delays = [], []
    for _ in range(n):
        delays.append(wait_random(max_delay))

    for future in asyncio.as_completed(delays):
        result = await future
        sort_delays.append(result)

    return sort_delays
