# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Учтите, что числа могут быть отрицательными
# Пример:
# 67.82 -> 23
# (-0.56) -> 11


digit = input('Введите число: ')

sum_digit = 0
for c in digit:
    if c >= '1' and c <= '9':   # 0 - исключаем не нужное
        sum_digit += int(c)
    
print(f'Сумма цифр числа {digit} равна {sum_digit}')