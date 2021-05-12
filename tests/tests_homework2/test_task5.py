import string

import pytest
from homeworks.homework2.task5 import custom_range


def test_that_custom_range_with_1args_returns_slice():
    """Testing that function custom_range behaves as range function"""
    assert custom_range(string.ascii_lowercase, "g") == ["a", "b", "c", "d", "e", "f"]


def test_that_custom_range_with_2args_returns_slice():
    """Testing that function custom_range behaves as range function"""
    assert custom_range(string.ascii_lowercase, "g", "p") == [
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
    ]


def test_that_custom_range_with_3args_and_negative_step_returns_slice():
    """Testing that function custom_range behaves as range function"""
    assert custom_range(string.ascii_lowercase, "p", "g", -2) == [
        "p",
        "n",
        "l",
        "j",
        "h",
    ]
