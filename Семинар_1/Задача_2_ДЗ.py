# 2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# Нужно написать таблицу истинности.

print('Проверка истиности выражения "¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z" для всех возможных значений предикат:\n')

for i in range(0b111 + 1):
    binary_string = format(i, '03b')
    x = int(binary_string[0])
    y = int(binary_string[1])
    z = int(binary_string[2])

    result = not (x or y or z) == (not x) and (not y) and (not z)
    print(f'¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z} есть {not (x or y or z) == (not x) and (not y) and (not z)}')