"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence
We guarantee, that the given sequence contain >= 0 integers inside.
"""

from math import sqrt


def check_fibonacci(data_to_process):
    """This function checked that given sequence is a Fibonacci sequence or not"""
    for element in data_to_process:
        if (
            sqrt(5 * (element ** 2) - 4) % 1 == 0
            or sqrt(5 * (element ** 2) + 4) % 1 == 0
        ):
            continue
        else:
            return False

    def _check_window(x: int, y: int, z: int) -> bool:
        return (x + y) == z

    a, b, c = data_to_process[0], data_to_process[1], data_to_process[2]
    while len(data_to_process) >= 3:
        if not _check_window(a, b, c):
            return False
        data_to_process = data_to_process[1:]
        if len(data_to_process) >= 3:
            a, b, c = b, c, data_to_process[2]
        else:
            return True
