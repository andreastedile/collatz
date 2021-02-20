from functools import lru_cache


def f(n):
    if n % 2 == 0:
        return int(n / 2)
    else:
        return int(3 * n + 1)


@lru_cache(maxsize=None)
def collatz(n):
    if n == 1:
        return [n]
    return [n] + collatz(f(n))
