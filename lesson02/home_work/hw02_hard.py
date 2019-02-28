# Hard
#
# Задача-1 Пользователь вводит текст, необходимо разбить его по словам и выдать статистику по тексту
# 1. Сколько слов в тексте?
# 2. Сколько букв английского алфавита в тексте?
import re


def split_text_by_words(text):
    words = re.split("\s+", text)  # потому что может быть больше одного пробела между словами
    regex = re.compile(r'[A-zА-яё]')  # потому что слова могут состоять только из букв
    for word in words:
        if regex.search(word):
            pass
        else:
            words.remove(word)
    return words

text = input("Input text: ")
words = split_text_by_words(text)
print(f"Words in text: {len(words)}")

regex = re.compile(r'[A-z]')
letter_count = 0
for letter in text:
    if regex.search(letter):
        letter_count += 1
print(f"Latin letters in text: {letter_count}")


# Задача-2 Пользователь вводит два текста, необходимо найти все слова, которые есть в обоих текстах. Без учета регистра


def lower_word(word):
    word = word.lower()
    return word


text1 = input("Input first text: ")
text2 = input("Input second text: ")

words1 = set(map(lower_word, split_text_by_words(text1)))
words2 = set(map(lower_word, split_text_by_words(text2)))

print(f"Words in both texts: {words1.intersection(words2)}")

# EXTRA
# Есть два словаря. Один это рецепт блюда, второй это список продуктов, которые есть в холодильнике.
#
# Ключ это название продукта, значение - это количество.
#
# Нужно сравнить два словаря и дать словарь, в котором будет список покупок
# Если для рецепта всё есть, то сказать что ничего не нужно
# Разницей по измерению гр, мл, шт. Пренебречь
