from homeworks.homework9.task3 import universal_file_counter


def test_universal_file_counter_without_tokenizer():
    assert universal_file_counter("tests/tests_homework9/test_file_HW_9_task3", "txt") == 4


def test_universal_file_counter_with_tokenizer():
    assert universal_file_counter("tests/tests_homework9/test_file_HW_9_task3", "txt", str.split) == 4
