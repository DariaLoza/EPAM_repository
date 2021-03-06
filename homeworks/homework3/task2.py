"""Here's a not very efficient calculation function that calculates something important.
Calculate total sum of
slow_calculate() of all numbers starting from 0 to 500. Calculation time should not take more than a minute. Use
functional capabilities of multiprocessing module. You are not allowed to modify slow_calculate function. """
import hashlib
import multiprocessing
import random
import struct
import time


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack("<" + "B" * len(data), data))


from multiprocessing import Pool


def make_it_faster():
    with Pool(16) as pool:
        result = sum(pool.imap(slow_calculate, range(500)))
        return result


if __name__ == "__main__":
    print(make_it_faster())

1024259
