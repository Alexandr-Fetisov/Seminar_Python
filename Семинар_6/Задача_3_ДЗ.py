# Вам нужно решить задачи с помощью лямбд, filter, map, zip, enumerate, list comprehension

# 3. Сформировать список из N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

import os
os.system('cls')


def result():
    i = 0
    while i < 1:
        try: 
            i = int(input('Введите число: '))
        except ValueError:
            print('Это не число')
    return i

def sequence(num):
    lst= list(map(lambda x: (-3) ** x, [exponent for exponent in range(num)]))
    return lst

print(sequence(result()))
