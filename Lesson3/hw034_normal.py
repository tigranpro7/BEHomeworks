# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут: 
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

import random
spisok = []
spisokvrem = []
uniquespisok = []
ind = 0
pol = 1
n=15
for n in range(n):
    chislo = random.randint(1, 15)
    spisok.append(chislo)
spisok2 = spisok[:]
new_spisok = list(set(spisok))

for elm in spisok:
    spisok2 = spisok[:pol-1] + spisok[pol:]
    pol = pol + 1
    for elm2 in spisok2:
        if elm == elm2:
            ind = 1
    if ind == 0:
        uniquespisok.append(elm)
    ind = 0


    
print(spisok)
print(new_spisok)
print(uniquespisok)