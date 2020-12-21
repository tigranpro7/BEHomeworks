# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

spisok = [1, 2, 3, 4, 5, 6, 7, 8, 9]
spisoknew = []
for elm in spisok:
    if elm % 2 == 0:
        elm = elm / 4
        spisoknew.append(elm)
    else:
        elm = elm * 2
        spisoknew.append(elm)
    
print(spisoknew)