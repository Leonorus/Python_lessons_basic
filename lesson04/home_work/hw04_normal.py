# NORMAL
# Задание-1:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.
import random

file = r"testfile"
huge_number = [str(random.randint(0, 9)) for i in range(0, 2501)]
with open(file, "w") as f:
    f.write("".join(huge_number))

with open(file, "r") as f:
    readed_number = f.read()

prev_char = ""
sequence = ""
longest_sequence = ""
for char in readed_number:
    if char == prev_char:
        sequence += char
        if len(sequence) > len(longest_sequence):
            longest_sequence = sequence
    else:
        sequence = char

    prev_char = char

print(longest_sequence)
# Задание-2
# Сформировать квадратную матрицу, в каждой строке которой находится ровно один ноль на случайном месте, остальные элементы
# тоже рандомные. Пользователь вводит размер
