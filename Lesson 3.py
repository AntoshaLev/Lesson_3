# Задание 1
nums = {
    "zero": "ноль",
    "one": "один",
    "two": "два",
    "three": "три",
    "four": "четыре",
    "five": "пять",
    "six": "шесть",
    "seven": "семь",
    "eight": "восемь",
    "nine": "девять",
    "ten": "десять"
}


def num_translate(eng_words):
    return nums.get(eng_words)


print(num_translate("zero"))


# Задание_2

def thesaurus(*names):
    res = {}
    for name in names:
        key = name[0].capitalize()
        if key not in res:
            res[key] = []
        res[key].append(name)
    return res


print(thesaurus("Иван", "Мария", "Петр", "Илья"))

# Задание_3

import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(num):
    jokes = []

    for i in range(num):
        cur_noun = random.choice(nouns)
        cur_adverb = random.choice(adverbs)
        cur_adjective = random.choice(adjectives)

    jokes.append(f'{cur_noun} {cur_adverb} {cur_adjective}')
    return jokes


print(get_jokes(3))
