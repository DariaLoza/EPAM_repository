import pytest
from homeworks.homework2.task2 import major_and_minor_elem


def test_that_function_returns_major_and_minor_elem():
    """Testing that list:1,1,2,3,3,3,5 returns major_and_minor_elem: (3,2)"""
    assert major_and_minor_elem([3, 2, 3]) == (3, 2)
