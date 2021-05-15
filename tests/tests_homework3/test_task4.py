from homeworks.homework3.task4 import is_armstrong


def test_that_function_is_armstrong_check_numbers():
    """Testing that function _is_armstrong check numbers"""
    assert is_armstrong(15) == "Is not Armstrong number"


def test_that_function_is_armstrong_check_numbers():
    """Testing that function _is_armstrong check numbers"""
    assert is_armstrong(9) == "Is Armstrong number"
