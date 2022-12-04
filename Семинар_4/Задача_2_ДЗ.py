# 2. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности. Не использовать множества. Постарайтесь решить за одно условие
# Пример:
# [1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]

# вывод только тех элементов, которые не повторяются (уникальны) в списке

# import random
# n = int(input("Введите кол-во чисел исходной последовательности: "))
# lst = []
# for i in range(n):
#     lst.append(random.randint(0, 15))
# print(f"Исходная последовательность: {lst}")
# newlst = []
# for i in lst:
#     if lst.count(i) < 2:
#         newlst.append(i)
# print(f"Список неповторяющихся элементов: {newlst}")

# вывод всех элементов списка без повторения таковых

import random

listNumbers = int(input("Введите кол-во чисел исходной последовательности: "))
lst = []
for i in range(listNumbers):
    lst.append(random.randint(0, 9))

def find_num(lst):
    """найти повторяющееся число"""
    result = []
    print(lst, end = ' -> ')
    for i in lst:
        if i not in result:
            result.append(i) 
    print(result)

find_num(lst)