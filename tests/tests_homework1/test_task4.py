from homeworks.homework1.task4 import check_sum_of_four


def test_positive():
    """Testing positive result"""
    assert check_sum_of_four([3, -6, 7], [0, -7, 6], [-5, 4, 9], [0, 8, 4]) == 2


def test_negative():
    """Testing negative result"""
    assert check_sum_of_four([0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]) == 81
