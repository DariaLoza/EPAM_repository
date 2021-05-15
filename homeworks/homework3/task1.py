"""In previous homework task 4, you wrote a cache function that remembers other function output value. Modify it to be a parametrized decorator, so that the following code:

@cache(times=3)
def some_function():
    pass
Would give out cached value up to times number only. Example:

@cache(times=2)
def f():
    return input('? ')   # careful with input() in python2, use raw_input() instead

>> f()
1
'1'
>> f()     # will remember previous value
'1'
>> f()     # but use it up to two times only
'1'
>> f()
? 2
'2'"""


def make_key(args, kwargs):
    return (args, tuple(sorted(kwargs.items())))


def cache(times=2):
    def wrapper(fun):
        cache_data = {}

        def inner(*args, **kwargs):
            key = make_key(args, kwargs)
            if key not in cache_data:
                result = fun(*args, **kwargs)
                cache_data[key] = [result, 0]
            result, called = cache_data[key]
            if called > times:
                return fun(*args, **kwargs)
            else:
                cache_data[key][1] += 1

        return inner

    return wrapper


@cache()
def foo(a, b):
    return a + b


print(foo(1, 3))
