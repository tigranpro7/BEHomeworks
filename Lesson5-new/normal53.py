# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.

import os
import random
fulldigit = ''
for digit in range(2500):
    digits = str(random.randint(0, 9))
    fulldigit = fulldigit + digits
path = os.path.join('files', 'file.txt')
f = open(path, 'w', encoding='UTF-8')
result = f.write(fulldigit)
f.close()