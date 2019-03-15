__author__ = "Воропаев Сергей Викторович"

import random
import math

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.

randInt = random.randint(0, 999999999)
print("Integer: ", randInt)
biggestNum = 0
while randInt > 0:
    nextInt = randInt % 10
    if biggestNum < nextInt:
        biggestNum = nextInt
    randInt = randInt // 10
print("Biggest number: ", biggestNum)
# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.
a = int(input("Input a: "))
b = int(input("Input b: "))
print("a = ", a, "b = ", b)
a, b = b, a
print("a = ", a, "b = ", b)
a, b = b, a
a += b
print("a = ", a - (a - b), "b = ", a - b)
#
# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4

print("ax² + bx + c = 0")
a = int(input("Input a: "))
b = int(input("Input b: "))
c = int(input("Input c: "))
print("{0}x² + {1}x + {2} = 0".format(a, b, c))

D = b ** 2 - 4 * a * c
if D == 0:
    x1 = -1 * b + math.sqrt(D) / 2 * a
    print("x1 = ", x1)
elif D > 0:
    x1 = ((-1 * b) + math.sqrt(D)) / (2 * a)
    x2 = ((-1 * b) - math.sqrt(D)) / (2 * a)
    print("x1 = ", x1, "x2 = ", x2)
else:
    print("Корней нет")
