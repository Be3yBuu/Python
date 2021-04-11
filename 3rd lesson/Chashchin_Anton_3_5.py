import random


def get_jokes(number, flag=0):
    """
    Function of jokes
    :param number: number of list objects we need (maximum 5)
    :param flag: if exists - no repeats
    :return: list of concat strings of 3 random words from pool
    """
    final_list = []
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    if flag:
        for i in range(0, number):
            final_list.append(nouns.pop(random.randint(0, 4-i)) + ' ' + adverbs.pop(random.randint(0, 4-i)) + ' ' +
                              adjectives.pop(random.randint(0, 4-i)))
    else:
        for i in range(0, number):
            final_list.append(nouns[random.randint(0, 4)]+' '+adverbs[random.randint(0, 4)]+' ' +
                              adjectives[random.randint(0, 4)])
    return final_list
