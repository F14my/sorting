from time import perf_counter
from typing import Callable


def timeit_once(func: Callable, *args, **kwargs) -> float:
    """Measure time for given function"""
    start = perf_counter()
    func(*args, **kwargs)
    return perf_counter() - start


def benchmark_sorts(arrays: dict[str, list], algos: dict[str, Callable]) -> dict[str, dict[str, float]]:
    """Benchmark sorting algorithm"""
    results = {}
    for algo_name, algo in algos.items():
        results[algo_name] = {}

        for array_name, array in arrays.items():
            time = timeit_once(algo, array)
            results[algo_name][array_name] = time

    return results

