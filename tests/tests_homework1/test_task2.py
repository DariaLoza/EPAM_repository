import pytest
from homeworks.homework1.task2 import check_fibonacci


def test_that_fibonacci_returns_true():
    """Testing True result"""
    assert check_fibonacci([2, 3, 5, 8, 13, 21, 34])


def test_1_that_fibonacci_returns_false():
    """Testing False result"""
    assert not check_fibonacci([2, 3, 8, 13, 21, 34])


def test_2_that_fibonacci_returns_false():
    """Testing False result"""
    assert not check_fibonacci([4, 6, 10])
