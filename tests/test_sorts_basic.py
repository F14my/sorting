import pytest
from src.sorting.sorts import bubble_sort, quick_sort, counting_sort, radix_sort, insertion_sort, bucket_sort, heap_sort
from src.generators import rand_float_array

@pytest.mark.parametrize("sort_func_int", [
    bubble_sort,
    quick_sort,
    counting_sort,
    radix_sort,
    insertion_sort,
    heap_sort,
])
def test_sort_int(sort_func_int):
    arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    result = sort_func_int(arr.copy())
    assert result == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

@pytest.mark.parametrize("sort_func_float", [
    bucket_sort,
])
def test_sort_float(sort_func_float):
    arr = rand_float_array(10)
    result = sort_func_float(arr.copy())
    assert result == sorted(arr)