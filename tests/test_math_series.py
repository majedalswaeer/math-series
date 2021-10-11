import pytest
from math_series import __version__
from math_series.series import fibonacci
from math_series.series import lucas
from math_series.series import sum_series


def test_version():
    assert __version__ == '0.1.0'

def test_zero_fibonacci():
    actual=fibonacci(0)
    expected=0
    assert actual==expected

def test_one_fibonacci():
    actual=fibonacci(1)
    expected=1
    assert actual==expected

def test_two_fibonacci():
    actual=fibonacci(2)
    expected=1
    assert actual==expected

def test_three_fibonacci():
    actual=fibonacci(3)
    expected=2
    assert actual==expected

def test_four_fibonacci():
    actual=fibonacci(4)
    expected=3
    assert actual==expected

def test_ten_fibonacci():
    actual=fibonacci(10)
    expected=55
    assert actual==expected 


def test_zero():
    actual=lucas(0)
    expected=2
    assert actual==expected

def test_one():
    actual=lucas(1)
    expected=1
    assert actual==expected

def test_two():
    actual=lucas(2)
    expected=3
    assert actual==expected

def test_three():
    actual=lucas(3)
    expected=4
    assert actual==expected

def test_four():
    actual=lucas(4)
    expected=7
    assert actual==expected

def test_ten():
    actual=lucas(10)
    expected=123
    assert actual==expected     


def test_one_sum_series():
    expected = 1
    actual = sum_series(1,0,1)
    assert expected == actual

def test_two_sum_series():
    expected = 3
    actual = sum_series(2,2,1)
    assert expected == actual

