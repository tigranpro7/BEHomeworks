
__author__ = 'Геворкян Тигран Гришаевич'

# Задача-3: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.

number1 = int(input('Введите число'))
last_big = 0
while number1  !=0:
    if number1 % 10 > (number1 //10) % 10:
        bigest_number = number1 % 10
    else:
        bigest_number = (number1 //10) % 10
    if last_big < bigest_number:
        last_big = bigest_number
    number1 = number1 // 10
print(last_big)