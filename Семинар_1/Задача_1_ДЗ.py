# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Дополнительно: можете проверить, что это действительно число, и что это действительно входит в нужный диапазон
# Пример:
# 6 -> да
# 7 -> да
# 1 -> нет

while True:
    day_num = int(input('Введите номер дня недели (от 1 до 7): '))

    if day_num >= 1 and day_num <= 7:
        break

    print('Некорректный ввод, повторите!')

if day_num == 6 or day_num == 7:
    print('Этот день выходной')
else:
    print('Этот день будний')



# #day_num = ''
# while day_num.isdigit() == False:
#  day_num = input('Enter a number: ')

# print('You entered {}'.format(day_num))    
