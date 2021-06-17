from homeworks.homework4.task4 import fizzbuzz


def test_fizzbuzz_function_with_5():
    assert fizzbuzz(5) == ["1", "2", "fizz", "4", "buzz"]


def test_fizzbuzz_function_with_6():
    assert fizzbuzz(6) == ["1", "2", "fizz", "4", "buzz", "fizz"]


def test_fizzbuzz_function_with_17():
    assert fizzbuzz(17) == ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz', '11', 'fizz', '13', '14', 'fizz buzz', '16', '17']