from homeworks.homework7.task2 import backspace_compare


def test_backspace_compare_1_True():
    assert backspace_compare("ab#c", "ad#c")


def test_backspace_compare_2_True():
    assert backspace_compare("a##c", "#a#c")


def test_backspace_compare_3_False():
    assert not backspace_compare("a#c", "b")
