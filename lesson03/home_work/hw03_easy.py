# EASY

# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.


def custom_round(number, signs):
    number_parts = str(number).split(".")
    inc = 0
    if len(number_parts) < 2:
        return number
    elif len(number_parts[1]) <= signs:
        return number
    if int(number_parts[1][signs]) >= 5:
        inc = float("0." + "0" * signs + "1")
    unrounded_number = number + inc
    rounded_number = float(str(unrounded_number)[:signs+3])
    return rounded_number


print(custom_round(0.9939567, 1))   # 1
print(custom_round(0.9939567, 3))   # 0.994
print(custom_round(10, 4))          # 10
print(custom_round(0.9939567, 8))   # 0.9939567

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


