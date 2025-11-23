import pytest
from src.sorting.sorts import bubble_sort, quick_sort, counting_sort, radix_sort, insertion_sort, bucket_sort, heap_sort
from src.generators import rand_float_array, rand_int_array


@pytest.mark.parametrize("sort_func_int", [
    bubble_sort,
    quick_sort,
    counting_sort,
    radix_sort,
    insertion_sort,
    heap_sort,
])
def test_sort_int(sort_func_int):
    arr = rand_int_array(10000, 0, 100000)
    result = sort_func_int(arr.copy())
    assert result == sorted(arr)


@pytest.mark.parametrize("sort_func_float", [
    bucket_sort,
])
def test_sort_float(sort_func_float):
    arr = rand_float_array(10000)
    result = sort_func_float(arr.copy())
    assert result == sorted(arr)
