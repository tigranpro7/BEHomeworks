# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

fruit_list1 = ['pineapple', 'orange', 'banana', 'apple']
fruit_list2 = ['apple', 'orange', 'mango']
fruit_list12 = [fruit for fruit in fruit_list1 if fruit in fruit_list2]
print(fruit_list12)
