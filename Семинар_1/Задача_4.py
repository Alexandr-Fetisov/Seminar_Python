# 4. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
# *Примеры:* 
# - 6,78 -> 7
# - 5 -> нет
# - 0,34 -> 3

number = float(input('введите число: '))
digit_first_float = int(number * 10) % 10
if number == int(number):
    print ('нет')
else:    
    print(digit_first_float)
