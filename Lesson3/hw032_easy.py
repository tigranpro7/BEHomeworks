# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

spisok1 = [1, 2, 6, 'Число', True, []]
spisok2 = [[], 2, 5, 7, 'Единица', 'Число']
for elms in spisok1:
    for elms2 in spisok2:
        if elms == elms2:
            spisok1.remove(elms)

print(spisok1)