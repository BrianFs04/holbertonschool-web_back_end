#!/usr/bin/env python3
"""make_multiplier, func"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns: A function that multiplies a float by multiplier"""
    def func(number: float) -> float:
        """Returns: number times multiplier"""
        return(number * multiplier)

    return func
