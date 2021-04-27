import sys


def write_csv(value):
    with open('bakery.csv', 'a', encoding='utf-8') as file:
        file.write(str(value)+'\n')


write_csv(sys.argv[1])
