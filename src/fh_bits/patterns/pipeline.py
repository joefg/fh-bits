from collections.abc import Callable
from functools import reduce


def compose(*func: Callable) -> Callable:
    return reduce(lambda f, g: lambda x: g(f(x)), func, lambda x: x)
