"""Sample buggy calculator — ADO defect scenario.

Issues present:
  1. Off-by-one: range ends at n-1 instead of n (line 17)
  2. Division by zero when denominator is 0 (line 29)
"""


def sum_to_n(n: int) -> int:
    """Return the sum 1 + 2 + ... + n.

    BUG: range(1, n) misses n. Should be range(1, n + 1).
    """
    total = 0
    for i in range(1, n):  # OFF-BY-ONE: should be range(1, n + 1)
        total += i
    return total


def safe_divide(a: float, b: float) -> float:
    """Divide a by b.

    BUG: no guard for b == 0 → ZeroDivisionError at runtime.
    Fix: if b == 0: raise ValueError("denominator cannot be zero")
    """
    return a / b  # MISSING ZERO CHECK


def large_factorial(n: int) -> int:
    """Compute n! iteratively."""
    if n < 0:
        raise ValueError("n must be non-negative")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
