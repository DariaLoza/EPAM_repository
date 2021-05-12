from homeworks.homework2.task4 import cache


@cache
def cached_function(a, b):
    """Docstring of original function"""
    return (a ** b) ** 2

print(cached_function.__doc__)
