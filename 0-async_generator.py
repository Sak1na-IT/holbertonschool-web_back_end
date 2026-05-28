#!/usr/bin/env python3
""" Async generator """
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ Loop 10 times, wait 1 second, yield random number """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
