# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

import random
old_list = list(random.randint(0,20) for _ in range(10))
new_list = list(el**2 for el in old_list)
print(old_list, '-->', new_list)