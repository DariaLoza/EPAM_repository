import pytest
from homeworks.homework3.task2 import make_it_faster


def test_slow_calculate():
    """Testing slow_calculate"""
    assert make_it_faster() == 1024259
