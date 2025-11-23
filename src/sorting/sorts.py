from typing import TypeVar, Callable, Optional, Any

T = TypeVar("T")


def compare(a: T, b: T, key: Optional[Callable[[T], Any]] = None, cmp: Optional[Callable[[T, T], int]] = None, ) -> int:
    """
    Universal comparison of two elements taking into account key/cmp.

    Args:
        a (T): first element
        b (T): second element
        key (Optional[Callable[[T], Any]]): key function
        cmp (Optional[Callable[[T, T], int]]): comparison function

    Returns:
        int: comparison result
        if a < b:
            return -1
        if a > b:
            return 1
        if a == b:
            return 0
    """
    if cmp is not None:
        return cmp(a, b)
    if key is not None:
        a, b = key(a), key(b)
    if a < b:
        return -1
    if a > b:
        return 1
    return 0


def is_greater(a: T, b: T, key: Optional[Callable[[T], Any]] = None,
               cmp: Optional[Callable[[T, T], int]] = None, ) -> bool:
    """
    Helpful function for comparing two elements
    Args:
        a (T): first element
        b (T): second element
        key (Optional[Callable[[T], Any]]): key function
        cmp (Optional[Callable[[T, T], int]]): comparison function

    Returns:
        bool: True if 'a' is greater than 'b'
    """
    return compare(a, b, key=key, cmp=cmp) > 0


def bubble_sort(arr: list[T], *, key: Optional[Callable[[T], Any]] = None,
                cmp: Optional[Callable[[T, T], int]] = None, ) -> list[T]:
    """
    Bubble sort algorithm

    Args:
        arr (list[T]): the array to be sorted
        key (Optional[Callable[[T], Any]]): key function
        cmp (Optional[Callable[[T, T], int]]): comparison function

    Returns:
        list[T]: the sorted array
    """
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if is_greater(arr[j], arr[j + 1], key, cmp):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def median(a: list[T], i: int, j: int, k: int, *, key: Optional[Callable[[T], Any]] = None,
           cmp: Optional[Callable[[T, T], int]] = None, ) -> int:
    """Median function to find the median(uses in quick sort)"""
    ai, aj, ak = a[i], a[j], a[k]

    def le(u: T, v: T) -> bool:
        return compare(u, v, key=key, cmp=cmp) <= 0

    if (le(ai, aj) and le(aj, ak)) or (le(ak, aj) and le(aj, ai)):
        return j
    if (le(aj, ai) and le(ai, ak)) or (le(ak, ai) and le(ai, aj)):
        return i
    return k


def quick_sort(arr: list[T], *, key: Optional[Callable[[T], Any]] = None,
               cmp: Optional[Callable[[T, T], int]] = None, ) -> list[T]:
    """
    Quick sort algorithm.

    Args:
        arr (list[T]): the array to be sorted
        key (Optional[Callable[[T], Any]]): key function
        cmp (Optional[Callable[[T, T], int]]): comparison function
    Returns:
        list[T]: the sorted array
    """
    n = len(arr)
    if n <= 1:
        return arr

    left, right = 0, n - 1
    mid = (left + right) // 2
    pivot_idx = median(arr, left, right, mid)
    pivot = arr[pivot_idx]

    less: list[T] = []
    middle: list[T] = []
    greater: list[T] = []

    for x in arr:
        c = compare(x, pivot, key=key, cmp=cmp)
        if c < 0:
            less.append(x)
        elif c == 0:
            middle.append(x)
        else:
            greater.append(x)

    return quick_sort(less, key=key, cmp=cmp) + middle + quick_sort(greater, key=key, cmp=cmp)


def counting_sort(arr: list[int]) -> list[int]:
    """
    Count sort algorithm

    Args:
        arr (list[int]): the array to be sorted

    Returns:
        list[int]: the sorted array
    """
    n = len(arr)
    max_value = max(arr)
    cnt_arr = [0] * (max_value + 1)
    ans = [0] * n
    for num in arr:
        cnt_arr[num] += 1
    for i in range(1, max_value + 1):
        cnt_arr[i] += cnt_arr[i - 1]
    for i in range(n - 1, -1, -1):
        ans[cnt_arr[arr[i]] - 1] = arr[i]
        cnt_arr[arr[i]] -= 1
    return ans


def radix_sort(arr: list[int], base: int = 10) -> list[int]:
    """
    Radix sort algorithm

    Args:
        arr (list[int]): the array to be sorted
        base (int, optional): base. Defaults to 10.

    Returns:
        list[int]: the sorted array
    """
    max_num = max(arr)
    max_digit = 0
    while base ** max_digit <= max_num:
        max_digit += 1
    bins = [[] for _ in range(base)]
    for i in range(0, max_digit):
        for x in arr:
            digit = (x // base ** i) % base
            bins[digit].append(x)
        arr = [x for queue in bins for x in queue]
        bins = [[] for _ in range(base)]
    return arr


def insertion_sort(arr: list[T], *, key: Optional[Callable[[T], Any]] = None,
                   cmp: Optional[Callable[[T, T], int]] = None, ) -> list[T]:
    """
    Insertion sort algorithm

    Args:
        arr (list[T]): the array to be sorted
        key (Optional[Callable[[T], Any]], optional): key function. Defaults to None.
        cmp (Optional[Callable[[T, T], Any]], optional): comparison function. Defaults to None.

    Returns:
        list[T]: the sorted array
    """
    for i in range(1, len(arr)):
        cur = arr[i]
        j = i - 1
        while j >= 0 and is_greater(arr[j], cur, key, cmp):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = cur
    return arr


def bucket_sort(arr: list[float], n: int | None = None) -> list[float]:
    """
    Bucket sort algorithm

    Args:
        arr (list[float]): the array to be sorted
        n (int, optional): n - count of buckets. Defaults to None

    Returns:
        list[float]: the sorted array
    """
    if n is None:
        n = len(arr)
    buckets = [[] for _ in range(n)]
    for num in arr:
        buckets[int(n * num)].append(num)

    for bucket in buckets:
        insertion_sort(bucket)

    arr = [num for bucket in buckets for num in bucket]
    return arr


def heapify(arr: list[T], n: int, i: int, *, key: Optional[Callable[[T], Any]] = None,
            cmp: Optional[Callable[[T, T], int]] = None, ) -> None:
    """
    The part of heap sort algorithm

    Args:
        arr (list[T]): the array to be sorted
        n (int): length of array
        i (int): index
        key (Optional[Callable[[T], Any]], optional): key function. Defaults to None.
        cmp (Optional[Callable[[T, T], Any]], optional): comparison function. Defaults to None.

    Returns:
        None
    """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and is_greater(arr[left], arr[largest], key, cmp):
        largest = left

    if right < n and is_greater(arr[right], arr[largest], key, cmp):
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest, key=key, cmp=cmp)


def heap_sort(arr: list[T], *, key: Optional[Callable[[T], Any]] = None,
              cmp: Optional[Callable[[T, T], int]] = None, ) -> list[T]:
    """
    Heap sort algorithm

    Args:
        arr (list[T]): the array to be sorted
        key (Optional[Callable[[T], Any]], optional): key function. Defaults to None.
        cmp (Optional[Callable[[T, T], Any]], optional): comparison function. Defaults to None.
    Returns:
        list[T]: the sorted array
    """
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, key=key, cmp=cmp)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0, key=key, cmp=cmp)

    return arr

