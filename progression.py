def sum_arithmetic_progression(n):
    if n <= 0:
        raise ValueError("Кількість членів має бути додатньою.")
    a = 2
    d = 2
    sum_n = n / 2 * (2 * a + (n - 1) * d)
    return sum_n
