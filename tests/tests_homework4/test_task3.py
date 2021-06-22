from homeworks.homework4.task3 import my_precious_logger


def test_OK_case(capsys):
    text = "OK"
    my_precious_logger(text)
    captured = capsys.readouterr()
    assert captured.out == "OK"


def test_error_case(capsys):
    text = "error: file not found"
    my_precious_logger(text)
    captured = capsys.readouterr()
    assert captured.err == "error: file not found"


def test_with_no_error_case(capsys):
    text = "no error found"
    my_precious_logger(text)
    captured = capsys.readouterr()
    assert captured.out == "no error found"
