"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.
Write a function that accept any iterable of unique values and then
it behaves as range function:
import string
assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']
"""


def custom_range(iterable, *args):
    iterable_list = list(iterable)
    if len(args) == 1:
        return iterable_list[: iterable_list.index(args[0])]
    if len(args) == 2:
        return iterable_list[
            iterable_list.index(args[0]) : iterable_list.index(args[1])
        ]
    if len(args) == 3:
        return iterable_list[
            iterable_list.index(args[0]) : iterable_list.index(args[1]) : (args[2])
        ]
