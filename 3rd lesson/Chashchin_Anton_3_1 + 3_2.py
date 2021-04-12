def num_translate(number):
    dictionary = {'zero': 'ноль',
                  'one': 'один',
                  'two': 'два',
                  'three': 'три',
                  'four': 'четыре',
                  'five': 'пять',
                  'six': 'шесть',
                  'seven': 'семь',
                  'eight': 'восемь',
                  'nine': 'девять',
                  'ten': 'десять'
                  }
    if number.lower() in dictionary:
        if number.istitle():
            print(dictionary[number.lower()].capitalize())
        else:
            print(dictionary[number])
    else:
        print(None)
