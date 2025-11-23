import pytest
from src.sorting.sorts import bubble_sort, quick_sort, counting_sort, radix_sort, insertion_sort, bucket_sort, heap_sort
from src.generators import rand_float_array

ALGOS = [bubble_sort, quick_sort, counting_sort, radix_sort, insertion_sort, heap_sort]


@pytest.mark.parametrize("sort_func_int", ALGOS)
def test_sort_int(sort_func_int):
    arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    result = sort_func_int(arr.copy())
    assert result == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_sort_float():
    arr = rand_float_array(10)
    result = bucket_sort(arr.copy())
    assert result == sorted(arr)


def test_radix_sort_base_10():
    arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    result = radix_sort(arr.copy())
    assert result == sorted(arr)


def test_radix_sort_base_2():
    arr = [100, 10101, 1, 10, 10101010, 1001]
    result = radix_sort(arr.copy(), 2)
    assert result == sorted(arr)


def test_radix_sort_base_12():
    arr = [144, 12, 1, 172, 35, 0, 83, 50]
    result = radix_sort(arr, base=12)
    expected = sorted(arr)
    assert result == expected
