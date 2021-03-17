#!/usr/bin/env python3
"""measure_runtime"""
from asyncio import gather
from time import perf_counter
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measures the total runtime and returns it"""
    s = perf_counter()
    await gather(async_comprehension())
    elapsed = perf_counter() - s
    return elapsed
