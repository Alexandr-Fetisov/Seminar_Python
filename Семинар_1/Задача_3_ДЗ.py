# 3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт
# номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# x=34; y=-30 -> 4
# x=2; y=4-> 1
# x=-34; y=-30 -> 3

while True:
    x = int(input('Введите X: '))
    y = int(input('Введите Y: '))

    if x != 0 and y != 0:
        break

    print('Хотя бы одна из координат не должна быть равна 0')

if x == 0:
    print('Точка лежит на оси OX')
elif y == 0:
    print('Точка лежит на оси OY')
elif x > 0 and y > 0:
    print('Точка лежит в 1 четверти координат')
elif x < 0 and y > 0:
    print('Точка лежит во 2 четверти координат')
elif x < 0 and y < 0:
    print('Точка лежит в 3 четверти координат')
else:
    print('Точка лежит в 4 четверти координат')