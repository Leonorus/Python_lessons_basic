# EASY

# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.


def custom_round(number, signs):
    number_parts = str(number).split(".")
    inc = 0
    if int(number_parts[1][signs]) >= 5:
        inc = 1
    number_parts[1] = str(int(str(number_parts[1][:signs])) + inc)
    rounded_number = float(".".join(number_parts))
    return rounded_number


print(custom_round(0.1239567, 4))

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def is_lucky_ticket(ticket):
    ticket_number = [int(n) for n in ticket]
    if sum(ticket_number[:3]) == sum(ticket_number[3:]):
        return True
    else:
        return False


ticket = input("Ticket number: ")
if is_lucky_ticket(ticket):
    print("Билет счастливый")
else:
    print("Билет не является счастливым")


