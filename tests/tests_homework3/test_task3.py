import pytest
from homeworks.homework3.task3 import make_filter, sample_data


def test_Helper_filter_class():
    """Testing helper filter class"""
    assert make_filter(name="polly", type="bird").apply(sample_data) == [
        {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"}
    ]
