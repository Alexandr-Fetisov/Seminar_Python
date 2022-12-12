# Вам нужно решить задачи с помощью лямбд, filter, map, zip, enumerate, list comprehension

# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

import os
os.system('cls')

from random import randrange
N = int(input('Введите размер списка N: '))
lst = [randrange(N) for i in range(N)]
print(f"Получен список {lst}")

result = []
for el_1, el_2 in zip(lst[:(N + 1) // 2], lst[N // 2:][::-1]):
    result.append(el_1 * el_2)
print(f"Произведений пар чисел {result}")



