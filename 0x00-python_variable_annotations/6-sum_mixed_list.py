#!/usr/bin/env python3
"""sum_mixed_list - sum all elements of a mixed list"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """Returns: list sum as a float"""
    return(sum(num for num in mxd_list))
