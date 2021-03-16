#!/usr/bin/env python3
"""task_wait_n"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Multiple coroutines at the same time with async using Tasks
    """
    sort_delays, tasks = [], []
    for _ in range(n):
        tasks.append(task_wait_random(max_delay))

    for future in asyncio.as_completed(tasks):
        result = await future
        sort_delays.append(result)

    return sort_delays
