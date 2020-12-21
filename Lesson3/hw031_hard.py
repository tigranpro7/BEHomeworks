# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

equation = 'y = x + 11111140.2121'
x = 2.5
# вычислите и выведите y
k = ''
b = ''
for letter in equation[4:]:
    if letter == 'x':
        break
    k = k + letter
if k == '':
    k = '1'
print(k)
for letter in equation[::-1]:
    if letter == ' ':
        break
    b = b + letter
print(b[::-1])
y = int(k) * x + float(b[::-1])
print(y)