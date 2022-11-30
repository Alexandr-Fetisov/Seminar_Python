# 5.Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

N = int(input('Введите размер списка N: '))

def fib(N):
    if not N:
        return 0

    if N < 0:
        return (-1) ** (-N + 1) * fib(-N)

    if N in (1, 2):
        return 1

    return fib(N - 1) + fib(N - 2)

neg_fib = []
for i in range(-N, N + 1):
    neg_fib.append(fib(i))
print("Список чисел Фибоначчи:")
print(neg_fib)