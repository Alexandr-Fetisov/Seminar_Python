# Вам нужно решить задачи с помощью лямбд, filter, map, zip, enumerate, list comprehension

# 6. Из списка выше оставьте только те пары, где сумма кортежа кратна 5
# Пример:
# [(10,25),(3,4),(4,1)] => [(10,25),(4,1)]

import os
os.system('cls')
import random

numbers = [random.randint(1, 10) for _ in range(10)] # при необходимости измените от 1 до 100, количеством 200
print(f'список -> {list(enumerate(numbers))}')
print(f'список пар, где сумма кортежа кратна 5 -> {list(filter(lambda x: (x[0]+x[1])%5==0, enumerate(numbers)))}')