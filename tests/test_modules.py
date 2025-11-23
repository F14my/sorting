import pytest
from src.sorting.modules import factorial, factorial_recursive, fibo, fibo_recursive


@pytest.mark.parametrize("func, n, expected", [
    (factorial, 5, 120),
    (factorial, 15, 1307674368000),
    (factorial_recursive, 5, 120),
    (factorial_recursive, 15, 1307674368000),
])
def test_factorial(func, n, expected):
    assert func(n) == expected


@pytest.mark.parametrize("func, n, expected", [
    (fibo, 5, 5),
    (fibo, 99, 218922995834555169026),
    (fibo_recursive, 5, 5),
    (fibo_recursive, 24, 46368),
])
def test_fibo(func, n, expected):
    assert func(n) == expected
