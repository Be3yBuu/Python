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
    if number.istitle():
        try:
            print(dictionary.pop(number.lower()).capitalize())
        except KeyError:
            print(None)
    else:
        print(dictionary.pop(number.lower(), None))