
# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

import random
old_list = [random.randint(-10,10) for _ in range(10)]
new_list = [el for el in old_list if el % 3 == 0 and el >= 0 and el % 4 != 0]
print(old_list, '-->', new_list)