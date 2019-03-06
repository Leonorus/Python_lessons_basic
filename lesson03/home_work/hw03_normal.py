#NORMAL

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1


def fibonacci_slice(start, end):
    fibonacci_list = []
    for i in range(start, end+1):
        fibonacci_list.append(fibonacci(i))
    return fibonacci_list


def fibonacci(n):
    return n   # изучаем перемножение матриц и бинарное возведение в степень


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def quick_sort(list_to_sort, start=False, end=False):

    if not start:
        start = 0
    if not end:
        end = len(list_to_sort) - 1
    i = start
    j = end
    base = list_to_sort[(start + end) // 2]
    while i <= j:
        while list_to_sort[i] < base:
            i += 1
        while list_to_sort[j] > base:
            j -= 1
        if i <= j:
            if list_to_sort[i] > list_to_sort[j]:
                list_to_sort[i], list_to_sort[j] = list_to_sort[j], list_to_sort[i]
            i += 1
            j -= 1

    if i < end:
        quick_sort(list_to_sort, i, end)
    if start < j:
        quick_sort(list_to_sort, start, j)

    return list_to_sort


print(quick_sort([5, 4, 3, 9, 0, 2, 1, 3, 3]))
