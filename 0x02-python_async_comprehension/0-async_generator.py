#!/usr/bin/env python3
"""async_generator"""
from typing import Generator
from asyncio import sleep
from random import uniform


async def async_generator() -> Generator[float, None, None]:
    """Coroutine that loops 10 times, each time asynchronously wait 1 second,
    then yield a random number between 0 and 10. Use the random module."""
    for _ in range(10):
        await sleep(1)
        yield uniform(0, 10)
