import pytest
from homeworks.homework2.task4 import cache
from homeworks.homework2.task4 import cached_function


def test_cache_function():
    cache_function = cache(cached_function)
    some = 100, 200
    val_1 = cache_function(*some)
    val_2 = cache_function(*some)
    assert val_1 is val_2
