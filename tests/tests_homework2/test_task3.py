from homeworks.homework2.task3 import combinations


def test_that_combinations_returns_all_possible_lists():
    """Testing that function combinations returns all possible lists of K items"""
    assert combinations([1, 2], [3, 4]) == [(1, 3), (1, 4), (2, 3), (2, 4)]
