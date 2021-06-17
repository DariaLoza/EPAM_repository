from homeworks.homework4.task4 import fizzbuzz


def test_fizzbuzz_function_with_5():
    assert fizzbuzz(5) == ["1", "2", "fizz", "4", "buzz"]

def test_fizzbuzz_function_with_6():
    assert fizzbuzz(6) == ["1", "2", "fizz", "4", "buzz", "fizz"]

def test_fizzbuzz_function_with_34():
    assert fizzbuzz(34) == ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz', '11', 'fizz', '13', '14', 'fizz', '16', '17', 'fizz', '19', 'buzz', 'fizz', '22', '23', 'fizz', 'buzz', '26', 'fizz', '28', '29', 'fizz', '31', '32', 'fizz', '34']
