from homeworks.homework7.task1 import example_tree, find_occurrences


def test_find_occurrences():
    assert find_occurrences(example_tree, "RED") == 6


def test_find_occurrences_no_element():
    assert find_occurrences(example_tree, "Loza") == 0
