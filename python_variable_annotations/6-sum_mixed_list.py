#!/usr/bin/env python3
"""Mixed list sum."""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Sum a list of ints and floats."""
    return float(sum(mxd_lst))
