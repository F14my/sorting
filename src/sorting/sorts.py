def bubble_sort(arr: list[int]) -> list[int]:
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def quick_sort(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    less = list(filter(lambda x: x < pivot, arr))
    middle = list(filter(lambda x: x == pivot, arr))
    greater = list(filter(lambda x: x > pivot, arr))
    return quick_sort(less) + middle + quick_sort(greater)


def count_sort(arr: list[int]) -> list[int]:
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
    max_digit = max([len(str(elem)) for elem in arr])
    bins = [[] for _ in range(base)]
    for i in range(0, max_digit):
        for x in arr:
            digit = (x // base ** i) % base
            bins[digit].append(x)
        arr = [x for queue in bins for x in queue]
        bins = [[] for _ in range(base)]
    return arr

def insertion_sort(arr: list[int]) -> list[int]:
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def bucket_sort(arr: list[float], n: int | None = None) -> list[float]:
    buckets = [[] for _ in range(n)]
    for num in arr:
        buckets[int(n * num)].append(num)


    for bucket in buckets:
        insertion_sort(bucket)

    arr = [num for bucket in buckets for num in bucket]
    return arr


def heapify(arr: list[int], n: int, i: int) -> None:
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr: list[int]) -> list[int]:
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

    return arr
