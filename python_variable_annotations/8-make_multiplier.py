#!/usr/bin/env python3
"""Multiplier function generator."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float."""
    def multiply_function(value: float) -> float:
        return value * multiplier
    return multiply_function
