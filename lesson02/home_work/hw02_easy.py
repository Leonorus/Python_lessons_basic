import random
# Easy
#
# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.
#
# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз
#
# Подсказка: воспользоваться f-строками
fruits = ['яблоко', 'банан', 'киви', 'арбуз']
maxLen = 0
for fruit in fruits:
    if len(fruit) > maxLen:
        maxLen = len(fruit)
i = 0
for fruit in fruits:
    print(f"{i+1}. {' ' * (maxLen-len(fruit))}{fruit}")
    i += 1
#
# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.
#


def generate_list():
    gen_list = [random.randint(-99, 99) for i in range(0, random.randint(10, 99))]
    return gen_list


list1 = generate_list()
list2 = generate_list()
print(f"list 1 = {list1} \nlist 2 = {list2}")
set1 = set(list1)
set2 = set(list2)
elements_to_remove = set1.intersection(set2)
print(f"Intersection: {elements_to_remove}")
for element in elements_to_remove:
    list1.remove(element)
print(f"list 1 = {list1}")
# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.


def element_converter(element):
    if element % 2 == 0:
        element = element / 4
    else:
        element = element * 2
    return element


rand_list = generate_list()
print(f"Generated list: {rand_list}")
result_list = list(map(element_converter, rand_list))
print(f"Converted list: {result_list}")
