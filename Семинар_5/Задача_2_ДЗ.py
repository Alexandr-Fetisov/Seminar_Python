# 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи:
# На столе лежит 2021(или сколько вы скажете) конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28(или сколько вы зададите в начале) конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

# Если делаете a и b - не нужно создавать отдельных файлов с полностью копированным кодом,
# лучше выделите в отдельные функции бота и умного бота.


import os
import random

def clear_screen():
    os.system('cls')

clear_screen()


print('Сыграем в конфеты.')
candy = int(input('Сколько конфет на столе разыгрываем? '))
motion = int(input('Сколько конфет можно брать за один ход? '))
print('Общее количество конфет :', candy,'\nВарианты игры:')
print('1 - игрок против игрока\n2 - игрок против бота\n3 - игрок против умного бота')
b = int(input('Введите вариант игры 1, 2 или 3: '))
print('Вы выбрали вариант', b,'')
pl = random.randint(1, 2)


def botsimple():
    global tes
    tes = random.randint(1, motion)
    return tes


def bot_ai():
    global tes
    tes = candy % (motion + 1)
    if tes == 0:
        tes += 1
    return tes


def human():
    global tes
    tes = int(input('Сколько конфет возьмете? '))
    return tes


while candy > 0:
    print('Конфет осталось', candy,'')
    pl += 1
    if pl % 2 == 0:
        print('Ходит 1 игрок')
        while True:
            play = int(input('Сколько конфет возьмете? '))
            if play > motion or play < 1 or play > candy:
                print('Введите другое число')
                continue
            break
        candy -= play
    else:
        print('Ходит 2 игрок')
        if b == 1:
            print(human())
            candy -= tes
        elif b == 2:
            tes = botsimple()
            while tes > motion:
                tes -= 1
            print('Бот взял', tes)
            candy -= tes
        elif b == 3:
            print(bot_ai())
            candy -= tes
if pl % 2 == 0:
    print('Победил 1 игрок')
else:
    print('Победил 2 игрок')