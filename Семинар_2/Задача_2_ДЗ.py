# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений (набор - это список) чисел от 1 до N.
# Не используйте функцию math.factorial.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] #(1, 1*2, 1*2*3, 1*2*3*4)

number = int(input('Введите число: '))

strk = '[1,'
proizv = 1
for i in range(2, number):
    proizv *= i
    strk += f' {proizv},'
strk += f' {proizv*number}]'

print(strk)
