# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    row_nach = [1, 1]
    while len(row_nach) != m:
        r = row_nach[-1] + row_nach[-2]
        row_nach.append(r)
    row_fin = row_nach[n-1:]
    return row_fin

print(fibonacci(5, 10))

