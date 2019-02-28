# Normal
#
# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4] Результат: [3, 5, 2]
#
import random
import math


def generate_list(length=0):
    gen_list = [random.randint(-99, 99) for i in range(0, random.randint(10, 99) if length == 0 else length)]
    return gen_list


def element_sqrt(element):
    try:
        element = math.sqrt(element)
    except ValueError:
        return None
    return element


def is_integer(element):
    try:
        if element.is_integer():
            return True
        else:
            return False
    except AttributeError:
        return False


generated_list = generate_list()
print(f"Generated list: {generated_list}")
result_list = list(map(int, (filter(is_integer, (map(element_sqrt, generated_list))))))
print(f"Squarted list: {result_list}")

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)


def add_zero(number):
    if number < 10:
        number = f"0{number}"
    return number


def number_to_word(number, type_of_convert):
    number_list = ["первое", "второе", "третье", "четвертое", "пятое", "шестое", "седьмое", "восьмое", "девятое",
                   "десятое",
                   "одиннадцатое", "двенадцатое", "тринадцатое", "четырнадцатое", "пятнадцаторе", "шестнадцатое",
                   "семнадцатое", "восемнадцатое", "девятнадцатое", "двадцатое"]
    dec_list = ["двадцать", "тридцать"]
    mounts = ["января", "февраля", "марта", "апреля", "мая", "июня", "июля", "августа", "сентября", "октября", "ноября",
              "декабря"]
    number = int(number)
    if type_of_convert == "day":
        if number <= 20:
            word = number_list[number - 1]
        else:
            word = f"{dec_list[number // 10 - 2]} {number_list[(number % 10) - 1]}"
    elif type_of_convert == "month":
        word = mounts[number - 1]
    return word


random_date = f"{add_zero(random.randint(1,31))}.{add_zero(random.randint(1,12))}.{random.randint(1,9999)}"
print(f"Random date: {random_date}")


splited_date = random_date.split(".")
print(f"{number_to_word(splited_date[0], 'day')} {number_to_word(splited_date[1], 'month')} {splited_date[2]} года")


#
# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random
#

def generate_list(length=False):
    gen_list = [random.randint(-100, 100) for i in range(0,  length if length else random.randint(10, 99))]
    return gen_list
