from homeworks.homework9.task1 import merge_sorted_files


def test_merge_sorted_files():
    assert merge_sorted_files(
        ["tests/tests_homework9/file1", "tests/tests_homework9/file2"]
    ) == [1, 2, 3, 4, 5, 6]
