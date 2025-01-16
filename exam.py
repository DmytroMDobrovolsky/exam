def sum_arithmetic_progression(n):
    
    a = 2
    
    d = 2
    
    sum_n = n / 2 * (2 * a + (n - 1) * d)
    return sum_n


try:
    n = int(input("Введіть кількість членів арифметичної прогресії (n): "))
    if n <= 0:
        print("Кількість членів має бути додатньою.")
    else:
        result = sum_arithmetic_progression(n)
        print(f"Сума перших {n} членів прогресії: {result}")
except ValueError:
    print("Будь ласка, введіть ціле число.")
