
# Задача-3:
# Напишите скрипт, отображающий папки текущей директории.

import os
path = os.getcwd()
spisok_papok = []

for elm in os.listdir():
    if os.path.isdir(elm) == True:
        spisok_papok.append(elm)
print(spisok_papok)
