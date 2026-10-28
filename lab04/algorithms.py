from functools import lru_cache


def tribonacci_recursive(n: int) -> int:
    """Чиста рекурсія без кешування (експоненційний час)."""
    if n == 0:
        return 0
    if n in (1, 2):
        return 1
    return (
        tribonacci_recursive(n - 1)
        + tribonacci_recursive(n - 2)
        + tribonacci_recursive(n - 3)
    )


@lru_cache(maxsize=None)  # noqa: UP033
def tribonacci_memoized(n: int) -> int:
    """Рекурсія з мемоізацією підзадач (лінійний час)."""
    if n == 0:
        return 0
    if n in (1, 2):
        return 1
    return (
        tribonacci_memoized(n - 1)
        + tribonacci_memoized(n - 2)
        + tribonacci_memoized(n - 3)
    )


def tribonacci_iterative(n: int) -> int:
    """Ітеративний підхід (безпечний для стеку, лінійний час)."""
    if n == 0:
        return 0
    if n in (1, 2):
        return 1

    a, b, c = 0, 1, 1
    for _ in range(3, n + 1):
        a, b, c = b, c, a + b + c
    return c
