__author__ = "Воропаев Сергей Викторович"


import random

# Дз от Пака

# EASY
# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.
#

randInt = random.randint(-99999999, 99999999)
print("Число: ", randInt)
randInt = abs(randInt)
while randInt > 0:
    print(randInt % 10)
    randInt = randInt // 10

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную
# или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

a = input("Введите первую переменную: ")
b = input("Введите вторую переменную: ")
print("a = ", a, "b = ", b)
c = a
a = b
b = c
print("a = ", a, "b = ", b)

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

age = int(input("Введите ваш возраст: "))
if age < 18:
    print("Доступ запрещен")
else:
    print("Доступ разрешен")
