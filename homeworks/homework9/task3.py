"""
Write a function that takes directory path, a file extension and an optional tokenizer.
It will count lines in all files with that extension if there are no tokenizer.
If a the tokenizer is not none, it will count tokens.
For dir with two files from hw1.py:
>>> universal_file_counter("tests/tests_homework9/test_file_HW_9_task3", "txt")
4
>>> universal_file_counter("tests/tests_homework9/test_file_HW_9_task3", "txt", str.split)
4
"""
from pathlib import Path
from typing import Callable, Optional


def line_by_line_tokenizer(file):
    counter = 0
    for line in file:
        counter += 1
    return counter


def universal_file_counter(
    dir_path: Path,
    file_extension: str,
    tokenizer: Optional[Callable] = line_by_line_tokenizer,
) -> int:
    counter = 0

    with open(dir_path, "r") as file:
        if tokenizer is True:
            counter += len(tokenizer(file.read))
            return counter
        else:
            return line_by_line_tokenizer(file)
