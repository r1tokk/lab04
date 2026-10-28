import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from algorithms import tribonacci_iterative, tribonacci_memoized, tribonacci_recursive


def test_base_cases() -> None:
    """Перевірка базової логіки на перших значеннях."""
    assert tribonacci_recursive(0) == 0
    assert tribonacci_recursive(1) == 1
    assert tribonacci_recursive(2) == 1


def test_tribonacci_sequence() -> None:
    """Перевірка послідовності Трібоначчі для перших 10 чисел."""
    expected = [0, 1, 1, 2, 4, 7, 13, 24, 44, 81]
    got = [tribonacci_memoized(i) for i in range(10)]
    assert got == expected


def test_iterative_matches_recursive() -> None:
    """Перевірка паритету між ітеративною та рекурсивною (кешованою) версіями."""
    for n in range(40):
        assert tribonacci_memoized(n) == tribonacci_iterative(n)


def test_cache_clear_behavior() -> None:
    """Перевірка доступності API кешу (cache_clear)."""
    tribonacci_memoized.cache_clear()
    tribonacci_memoized(5)
    info = tribonacci_memoized.cache_info()

    assert info.misses > 0
    assert info.currsize > 0

    tribonacci_memoized.cache_clear()
    cleared_info = tribonacci_memoized.cache_info()
    assert cleared_info.hits == 0
    assert cleared_info.misses == 0
    assert cleared_info.currsize == 0


def test_edge_cases() -> None:
    """Перевірка на нульових вхідних даних (граничний випадок)."""
    assert tribonacci_iterative(0) == 0
    assert tribonacci_memoized(0) == 0
