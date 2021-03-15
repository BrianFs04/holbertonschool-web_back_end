#!/usr/bin/env python3
"""zoom_array - Annotate function"""
from typing import List


def zoom_array(lst: List, factor: int = 2) -> List:
    """Prints every number of a list in accordance with the factor number
    Returns: The list zoomed in
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
