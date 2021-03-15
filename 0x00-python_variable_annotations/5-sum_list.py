#!/usr/bin/env python3
"""sum_list: sum all elements of a list"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Returns: list sum as a float """
    return(sum(num for num in input_list))
