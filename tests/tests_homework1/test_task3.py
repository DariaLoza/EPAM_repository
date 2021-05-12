import pytest
from homeworks.homework1.task3 import find_maximum_and_minimum


def test_1():
    """Testing check1"""
    assert find_maximum_and_minimum('check1.txt') == (1, 9)



def test_2():
    """Testing check2"""
    assert find_maximum_and_minimum('check2.txt') == (-6, 9)
