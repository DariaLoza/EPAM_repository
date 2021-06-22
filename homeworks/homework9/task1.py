"""
Write a function that merges integer from sorted files and returns an iterator
file1.txt:
1
3
5
file2.txt:
2
4
6
>>list(merge_sorted_files(["file1.txt", "file2.txt"]))
[1, 2, 3, 4, 5, 6]
"""
import math
from pathlib import Path
from typing import Iterator


def list_on_two_parts(lst, c_num):
    n = math.ceil(len(lst) / c_num)

    for x in range(0, len(lst), n):
        e_c = lst[x : n + x]

        if len(e_c) < n:
            e_c = e_c + [None for y in range(n - len(e_c))]
        yield e_c


def merge_sorted_files(file_list: [str, str]) -> Iterator:
    list_of_numbers = []
    for files in file_list:
        file = Path(files)
        file = file.read_text().splitlines()
        for i in file:
            list_of_numbers.append(int(i))
    return sorted(list_of_numbers)

