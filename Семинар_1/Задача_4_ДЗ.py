# 4. Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).
# Пример:
# - quarter = 1 => x∈(0, ∞) u y∈(0,∞)

while True:
    quarter = int(input('Введите номер четверти (1-4): '))

    if quarter in [1, 2, 3, 4]:
        break

    print('Некорректный ввод, повторите!')

if quarter == 1:
    print('Координата X может быть от 0 до плюс бесконечности')
    print('Координата Y может быть от 0 до плюс бесконечности')
elif quarter == 2:
    print('Координата X может быть от минус бесконечности до 0')
    print('Координата Y может быть от 0 до плюс бесконечности')
elif quarter == 3:
    print('Координата X может быть от минус бесконечности до 0')
    print('Координата Y может быть от минус бесконечности до 0')
else:
    print('Координата X может быть от 0 до плюс бесконечности')
    print('Координата Y может быть от минус бесконечности до 0')