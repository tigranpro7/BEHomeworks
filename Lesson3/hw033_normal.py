# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

import random
spisok = []
n=10
for n in range(n):
    chislo = random.randint(-100, 100)
    spisok.append(chislo)
print(spisok)

