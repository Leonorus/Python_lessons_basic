
__author__ = 'Воропаев Сергей Викторович'

# Задание-1:
# Пользователь вводит число определите, является ли данное число простым. Делится только на себя и на единицу

integer = int(input("Введите число: "))
divisors = []
divisor = integer

while divisor > 0:
    if integer % divisor == 0:
        divisors.append(divisor)
    divisor -= 1


if len(divisors) <= 2:
    print("Число является простым")
else:
    print("Число не является простым")
# Задание-2
# Найдите n-ое число Фибоначчи

n = int(input("Введите n:"))
i = 0
int1 = int2 = 1
if n > 2:
    while i < n:
        int_sum = int1 + int2
        int1 = int2
        int2 = int_sum
        i += 1
print(int2)

# Задание-3
# Вывести на экран:
# AAABBBAAABBBAAABBB
# BBBAAABBBAAABBBAAA
# AAABBBAAABBBAAABBB
# (таких строк n, в каждой строке m троек AAA)

n = int(input("Введите n: "))
m = int(input("Введите m: "))

i = 0
while i < n:
    if i % 2 == 0:
        print("BBBAAA" * m)
    else:
        print("AAABBB" * m)
    i += 1
