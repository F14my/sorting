import random


def rand_int_array(n: int, lo: int, hi: int, *, distinct=False, seed=None) -> list[int]:
    """
    Generate random integer array
    Args:
        n (int): length of array
        lo (int): lower bound of array
        hi (int): upper bound of array
        distinct (bool, optional): whether to generate distinct numbers. Defaults to False.
        seed (int, optional): random seed. Defaults to None.

    Returns:
        list[int]: array of random integers
    """

    if lo > hi:
        raise ValueError(f"lo ({lo}) must be <= hi ({hi})")

    if seed is not None:
        random.seed(seed)

    if distinct:
        max_unique = hi - lo + 1
        if n > max_unique:
            raise ValueError(
                f"cannot generate {n} distinct numbers in range [{lo}, {hi}] "
                f"(only {max_unique} unique values possible)"
            )
        return random.sample(range(lo, hi + 1), n)

    return [random.randint(lo, hi) for _ in range(n)]


def nearly_sorted(n: int, swaps: int, *, seed=None) -> list[int]:
    """
    Generate nearly sorted array
    Args:
        n (int): length of array
        swaps (int): number of swaps
        seed (int, optional): random seed. Defaults to None.
    Returns:
        list[int]: array of nearly sorted integers
    """

    if seed is not None:
        random.seed(seed)

    arr = list(range(n))
    for _ in range(swaps):
        i = random.randint(0, n - 1)
        j = random.randint(0, n - 1)
        arr[i], arr[j] = arr[j], arr[i]

    return arr


def many_duplicates(n: int, k_unique=5, *, lo: int = 0, hi: int = 100, seed=None) -> list[int]:
    """
    Generate many duplicate numbers
    Args:
        n (int): length of array
        k_unique (int, optional): number of unique numbers. Defaults to 5.
        lo (int, optional): lower bound of array
        hi (int, optional): upper bound of array
        seed (int, optional): random seed. Defaults to None.
    Returns:
        list[int]: array of many duplicate numbers
    """

    if seed is not None:
        random.seed(seed)

    if k_unique <= 0:
        raise ValueError(f"k_unique ({k_unique}) must be > 0")

    if lo > hi:
        raise ValueError(f"lo ({lo}) must be <= hi ({hi})")

    if k_unique > (hi - lo + 1):
        raise ValueError(f"k_unique ({k_unique}) is more than the available numbers in the range ({hi - lo + 1})")

    unique = random.sample(range(lo, hi + 1), k_unique)
    return [random.choice(unique) for _ in range(n)]


def reverse_sorted(n: int) -> list[int]:
    """
    Generate reverse sorted array
    Args:
        n (int): length of array
    Returns:
        list[int]: array of reverse sorted integers
    """

    if n <= 0:
        raise ValueError(f"n ({n}) must be > 0")
    arr = list(range(n))[-1::-1]
    return arr


def rand_float_array(n: int, lo=0.0, hi=1.0, *, seed=None) -> list[float]:
    """
    Generate random float array
    Args:
        n (int): length of array
        lo (float, optional): lower bound of array
        hi (float, optional): upper bound of array
        seed (int, optional): random seed. Defaults to None.
    Returns:
        list[float]: array of random floats
    """
    if seed is not None:
        random.seed(seed)

    if hi > 1.0:
        raise ValueError(f"hi ({hi}) must be <= 1.0")

    if lo < 0.0:
        raise ValueError(f"lo ({lo}) must be >= 0.0")

    if lo > hi:
        raise ValueError(f"lo ({lo}) must be <= hi ({hi})")

    return [random.uniform(lo, hi) for _ in range(n)]

