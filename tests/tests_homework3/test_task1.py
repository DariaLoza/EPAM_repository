from unittest.mock import Mock, call

from homeworks.homework3.task1 import cache


def test_cached():
    mock = Mock()
    cached_function = cache(times=1)(mock)
    cached_function(1, 3)
    cached_function(1, 3)
    cached_function(1, 3)
    assert mock.mock_calls == [call(1, 3), call(1, 3)]


def test_cached_with_same_arguments():
    mock = Mock()
    cached_function = cache(times=1)(mock)
    cached_function(1, 3)
    cached_function(1, 3)
    cached_function(1, 3)
    assert mock.mock_calls == [call(1, 3), call(1, 3)]


def test_not_cached_with_different_arguments():
    mock = Mock()
    cached_function = cache(times=1)(mock)
    cached_function(1, 3)
    cached_function(3, 1)
    cached_function(1, 3)
    cached_function(3, 1)
    assert mock.mock_calls == [call(1, 3), call(3, 1)]
