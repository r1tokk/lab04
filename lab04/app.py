import time
from collections.abc import Callable

from algorithms import tribonacci_iterative, tribonacci_memoized, tribonacci_recursive


def measure_time(func: Callable[[int], int], n: int) -> float:
    """Вимірює час виконання функції."""
    start = time.perf_counter()
    func(n)
    return time.perf_counter() - start


def main() -> None:
    ns = [20, 30, 35]

    print("Порівняння часу виконання (Трібоначчі)")
    print(
        f"{'n':<5} | {'Без кешу (с)':<20} | {'З lru_cache (с)':<20} | {'Ітеративно (с)':<20}"
    )
    print("-" * 75)

    for n in ns:
        tribonacci_memoized.cache_clear()
        t_memo = measure_time(tribonacci_memoized, n)

        t_iter = measure_time(tribonacci_iterative, n)
        t_rec = measure_time(tribonacci_recursive, n)

        print(f"{n:<5} | {t_rec:<20.5f} | {t_memo:<20.8f} | {t_iter:<20.8f}")

    print("Демонстрація роботи кешу (cache_info)")
    tribonacci_memoized.cache_clear()
    print("До виклику:", tribonacci_memoized.cache_info())

    tribonacci_memoized(30)
    print("Після першого обчислення (fib(30)):", tribonacci_memoized.cache_info())

    tribonacci_memoized(30)
    print("Після повторного виклику (взяття з кешу):", tribonacci_memoized.cache_info())


if __name__ == "__main__":
    main()
