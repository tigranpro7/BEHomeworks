
__author__ = 'Геворкян Тигран Гришаевич'

# Задача-2: Напишите программу, которая спрашивает "Четные или нечетные?", в зависимости от ответа,
# используя цикл с предусловием while или for in
# вывести в одну строку через пробел соотвествующие числа от 0 до 20
# Пример работы:
# $ "Четные или нечетные?"
# четные
# 0 2 4 6 8 10 12 14 16 18 20
# $ "Четные или нечетные?"
# нечетные
# 1 3 5 7 9 11 13 15 17 19
# $ "Четные или нечетные?"
# qwerty (или любая другая строка)
# Я не понимаю, что вы от меня хотите...

otvet = input('Четные или нечетные?')
if otvet == 'четные':
    for cifra in range(21):
        m = cifra % 2
        if m == 0:
            print(cifra)
elif otvet == 'нечетные':
    for cifra in range(21):
        m = cifra % 2
        if m == 1:
            print(cifra)
else:
    print('Я не понимаю, что вы от меня хотите...')
