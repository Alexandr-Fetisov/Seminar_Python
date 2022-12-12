# Вам нужно решить задачи с помощью лямбд, filter, map, zip, enumerate, list comprehension

# 5. Есть список случайных чисел в промежутке от 1 до 100, количеством 200. Создайте список кортежей,
# первый элемент которого - индекс элемента, а второй - сам элемент, при условии, что они не совпадают.
# [1,1,1,1] -> [(0,1),(1,1),(2,1),(3,1)] -> [(0,1),(2,1),(3,1)]

import os
os.system('cls')
import random

# numbers = [1, 1, 1, 1]
numbers = [random.randint(1, 10) for _ in range(10)] # при необходимости измените от 1 до 100, количеством 200
print(f'список -> {list(enumerate(numbers))}')
print(f'список без совпадений -> {list(filter(lambda x: x[0] != x[1], enumerate(numbers)))}')
print(f'список удаленных совпадений -> {list(filter(lambda x: x[0] == x[1], enumerate(numbers)))}')   

# оставшиеся кортежи перенумеровываем по порядку
# product = list(filter(lambda x: x[0] != x[1], enumerate(numbers)))
# count, numbers = zip(*product) 
# print(f'результирующий список -> {list(enumerate(numbers))}')