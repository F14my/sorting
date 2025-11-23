from typing import Callable
from src.sorting.sorts import bubble_sort, quick_sort, count_sort, radix_sort, insertion_sort, bucket_sort, heap_sort
from src.generators import rand_int_array, nearly_sorted, many_duplicates, reverse_sorted, rand_float_array

ALGOS: dict[str, Callable] = {
    "bubble": bubble_sort,
    "quick": quick_sort,
    "count": count_sort,
    "radix": radix_sort,
    "insertion": insertion_sort,
    "bucket": bucket_sort,
    "heap": heap_sort,
}

INT_ARRAY_TYPES: dict[str, Callable] = {
    "rand_int": lambda n: rand_int_array(n, 0, n),
    "nearly": lambda n: nearly_sorted(n, swaps=n // 30),
    "duplicates": lambda n: many_duplicates(n, k_unique=5),
    "reverse": lambda n: reverse_sorted(n),
}

FLOAT_ARRAY_TYPES: dict[str, Callable] = {
    "rand_float": lambda n: rand_float_array(n, 0.0, 1.0),
}
