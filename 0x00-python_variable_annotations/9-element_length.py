#!/usr/bin/env python3
"""Annotate a function"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns: the values of a list of tuples and the tuple length"""
    return [(i, len(i)) for i in lst]
