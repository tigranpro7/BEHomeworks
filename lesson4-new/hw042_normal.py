# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    fin_list = []
    the_list = origin_list.copy()
    n = 0
    while n < len(origin_list):
        n = n + 1
        min = float("inf")
        for elm in the_list:
            if elm < min:
                min = elm
        the_list.remove(min)
        fin_list.append(min)
    return fin_list



print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))