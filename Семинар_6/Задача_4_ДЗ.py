# Вам нужно решить задачи с помощью лямбд, filter, map, zip, enumerate, list comprehension

# 4. Дан список URL различных сайтов. Нужно составить список доменных имен сайтов.

import os
os.system('cls')

url_list = ['https://gb.ru/lessons/284811/homework',
            'https://volzhankarus.ru/spinningi-volzhanka/',
            'https://www.kinopoisk.ru/series/1355059/?from_block=trailer_promo',
            'https://www.youtube.com/watch?v=JuD-vOunzQw',
            'https://uteka.ru/catalog/medicinskie-izdeliya/',
            'https://www.ilovepdf.com/ru/split_pdf',
            'https://2gis.ru/VDN?m=37.708579%2C55.551158%2F13.84',            
            'https://www.softportal.com/dlcategory-603-1-0-0-0.html',
            'https://www.1tv.ru/movies',
            'https://www.rbc.ru/textonlines/12/12/2022/6216fb4d9a79474dc80e8821?from=from_main_2',
            'https://undetectable.io/ru/top-websites']
            

domen_list = list(map(lambda i: i[:i.find('/')], [i for i in map(lambda i: i.replace('https://',''), url_list)]))
print(domen_list)