# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
#     Примеры:
#     - 1, 4, 8, 7, 5 -> 8
#     - 78, 55, 36, 90, 2 -> 90

numbers = input('Введите через пробел 5 чисел: ')
numbers = numbers.split(' ')
maximum = int(numbers[0])
for i in numbers:
    i = int(i)
    if maximum < i:
        maximum = i
print (maximum)
