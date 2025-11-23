def factorial(n: int) -> int:
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

def factorial_recursive(n: int) -> int:
    if n == 0:
        return 1
    return n * factorial_recursive(n - 1)

def fibo(n: int) -> int:
    res = [0, 1]
    for i in range(2, n + 1):
        res.append(res[i - 1] + res[i - 2])
    return res[n]

def fibo_recursive(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo_recursive(n - 1) + fibo_recursive(n - 2)
