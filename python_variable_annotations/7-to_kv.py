#!/usr/bin/env python3
"""String and numerical value to tuple."""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple of a string and the square of v."""
    return (k, float(v ** 2))
