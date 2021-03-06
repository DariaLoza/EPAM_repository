"""
Write a function that takes a number N as an input and returns N FizzBuzz numbers*
Write a doctest for that function.
Definition of done:
 - function is created
 - function is properly formatted
 - function has doctests
 - doctests are run with pytest command
You will learn:
 - the most common test task for developers
 - how to write doctests
 - how to run doctests
assert fizzbuzz(5) == ["1", "2", "fizz", "4", "buzz"]
https://en.wikipedia.org/wiki/Fizz_buzz
** Энциклопедия профессора Фортрана page 14, 15, "Робот Фортран, чисть картошку!"
"""
from typing import List


def fizzbuzz(n: int) -> List[str]:
    fizz_buzz_list = []
    for i in range(1, n + 1):
        if i % 5 == 0 and i % 3 == 0:
            fizz_buzz_list.append("fizz buzz")
        elif i % 3 == 0:
            fizz_buzz_list.append("fizz")
        elif i % 5 == 0:
            fizz_buzz_list.append("buzz")
        else:
            fizz_buzz_list.append(str(i))
    return fizz_buzz_list


print(fizzbuzz(17))
