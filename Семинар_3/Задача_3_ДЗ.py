# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18
# [4.07, 5.1, 8.2444, 6.9814] - 0.9114 или 9114

import random
N = int(input('Введите размер списка N: '))
list = []
for i in range(N):
    list.append(round(random.uniform(0, 10), 3))
min = list[0]-int(list[0])
max = list[0]-int(list[0])

for item in list:
    if item-int(item) <= min:
        min = round(item-int(item), 3)
    if item-int(item) >= max:
        max = round(item-int(item), 3)
res = 0
res = round(max-min, 4)
print(f'Получен список {list} \nMax {max} и Min {min} дробная часть списка\nИх разница {res}')