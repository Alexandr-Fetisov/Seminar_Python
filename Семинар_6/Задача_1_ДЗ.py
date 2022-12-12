# Вам нужно решить задачи с помощью лямбд, filter, map, zip, enumerate, list comprehension

# 1. Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Пример:
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1


import os
os.system('cls')


list_a = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
findstr_a = "qwe"
try:
    a = list(filter(lambda tuple: tuple[0] == findstr_a, zip(list_a, range(len(list_a)))))
    print(f'Позиция второго вхождения "{findstr_a}": {a[1][1]}')
except:
    print(f'Второе вхождение "{findstr_a}" не найдено')


list_b = ["йцу", "фыв", "ячс", "цук", "йцукен"]
findstr_b = "йцу"
try:
    b = list(filter(lambda tuple: tuple[0] == findstr_b, zip(list_b, range(len(list_b)))))
    print(f'Позиция второго вхождения "{findstr_b}": {b[1][1]}')
except:
    print(f'Второе вхождение "{findstr_b}" не найдено')    



