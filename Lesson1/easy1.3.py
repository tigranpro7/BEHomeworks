# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4

# TODO: 
import math 
Ast = input ('Введите значение переменной a уравнения : ax² + bx + c = 0: ')
Bst = input ('Введите значение переменной b уравнения : ax² + bx + c = 0: ')
Cst = input ('Введите значение переменной c уравнения : ax² + bx + c = 0: ')
a = int(Ast)
b = int(Bst)
c = int(Cst)
x1 = (- b + math.sqrt(b**2 - 4*a*c))/(2*a)
x2 = (- b - math.sqrt(b**2 - 4*a*c))/(2*a)
print (x1, x2)
