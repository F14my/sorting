import pytest
from src.sorting.sorts import bubble_sort, insertion_sort, heap_sort, quick_sort

ALGOS = [bubble_sort, insertion_sort, heap_sort, quick_sort]
@pytest.mark.parametrize("sort_func", ALGOS)
def test_sort_key_len(sort_func):
    data = ["aaa", "b", "cccc", "dd"]
    result = sort_func(data.copy(), key=len)
    assert result == ["b", "dd", "aaa", "cccc"]

@pytest.mark.parametrize("sort_func", ALGOS)
def test_sort_key_abs(sort_func):
    data = [3, -1, -5, 2, 0]
    result = sort_func(data.copy(), key=abs)
    assert result == [0, -1, 2, 3, -5]


def even_odd_cmp(a: int, b: int) -> int:
    if a % 2 == 0 and b % 2 != 0:
        return -1
    if a % 2 != 0 and b % 2 == 0:
        return 1
    if a > b:
        return 1
    if a < b:
        return -1
    return 0

@pytest.mark.parametrize("sort_func", ALGOS)
def test_sort_cmp_even_odd(sort_func):
    data = [5, 2, 7, 4, 3, 6, 1]
    result = sort_func(data.copy(), cmp=even_odd_cmp)
    assert result == [2, 4, 6, 1, 3, 5, 7]

def reverse_cmp(a, b) -> int:
    if b > a:
        return 1
    if b < a:
        return -1
    return 0

@pytest.mark.parametrize("sort_func", ALGOS)
def test_sort_cmp_reverse(sort_func):
    data = [1, 4, 2, 3]
    result = sort_func(data.copy(), cmp=reverse_cmp)
    assert result == [4, 3, 2, 1]
