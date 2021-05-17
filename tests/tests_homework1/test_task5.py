from homeworks.homework1.task5 import find_maximal_subarray_sum


def test_1_find_maximal_subarray_sum():
    """Testing that function find maximal subarray sum"""
    assert find_maximal_subarray_sum([1, 3, -1, -3, 5, 3, 6, 7], 3) == 16


def test_2_find_maximal_subarray_sum():
    """Testing that function find maximal subarray sum"""
    assert find_maximal_subarray_sum([1, 20, 20, -3, 5, 3], 6) == 46


def test_find_maximal_subarray_sum_3_with_0():
    """Testing that function find maximal subarray sum"""
    assert find_maximal_subarray_sum([0, 0, 0, 0, 0, 0, 0, 0], 3) == 0
