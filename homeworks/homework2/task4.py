from functools import wraps


def cache(cached_function):
    stored_value = []

    @wraps(cached_function)
    def wrapped(*args, **kwargs):
        nonlocal stored_value

        key_of_call = (args, kwargs)
        for key, value in stored_value:
            if key == key_of_call:
                return value
        else:
            result = cached_function(*args, **kwargs)
            stored_value.append((key_of_call, result))
            return result

    return wrapped


def cached_function(a, b):
    """Docstring of original function"""
    return (a ** b) ** 2
