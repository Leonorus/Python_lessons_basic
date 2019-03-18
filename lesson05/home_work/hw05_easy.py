# EASY
# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
# Учесть проверку на то что папка не пуста и на то, что такая папка уже существует
import os
import re

while True:
    print("1. Create dirs\n" "2. Remove dirs\n" "3. Quit")
    userComand = int(input("Enter action: "))

    if userComand == 1:
        for i in range(0, 10):
            if not os._exists(f"dir_{i}"):
                os.mkdir(f"dir_{i}")
    elif userComand == 2:
        for dir in os.listdir("."):
            if re.match("dir_[0-9]", dir):
                if not os.listdir(dir):
                    os.rmdir(dir)
    elif userComand == 3:
        exit()
    else:
        print("Please input number of action")


# Задача-2:
# Напишите скрипт, который выводит в консоль список файлов и папок в указанной директории.

directory = input("Enter directory to list: ")
for file in os.listdir(directory):
    print(file)
