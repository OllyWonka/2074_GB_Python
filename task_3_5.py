import random


def get_jokes(count: int) -> list:
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    list_out = []

    count = list(map(random.choice, [nouns, adverbs, adjectives]))
    list_out.append(' '.join(count))
    return list_out


print(get_jokes(2))
print(get_jokes(10))
