# 1. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# Пример:
# N = 20 -> [2, 5]
# N = 30 -> [2, 3, 5]


import os
import math as mt


def input_int(msg: str) -> int:
    """запрос целочисленного числа"""
    return int(input(msg))

def get_multipliers(n):
    """поиск множителей"""
    fact = []

    for i in range(2, int(mt.sqrt(n))+1):
        while n % i == 0:
            n = n / i
            fact.append(i)

    if (n > 1):
        fact.append(int(n))

    return fact


os.system('cls')

num = input_int('Введите натуральное число N: ')
print(get_multipliers(num))
