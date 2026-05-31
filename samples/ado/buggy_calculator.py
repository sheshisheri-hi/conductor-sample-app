def sum_to_n(n):
    # Returns the sum of numbers from 1 to n inclusive
    return sum(range(1, n + 1))  # WHY: Fixed off-by-one error; range should include n
