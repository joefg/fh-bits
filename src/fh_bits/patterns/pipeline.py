from functools import reduce
from typing import Callable

def compose(*func: Callable) -> Callable:
    return reduce(lambda f, g: lambda x: g(f(x)), func, lambda x: x)
