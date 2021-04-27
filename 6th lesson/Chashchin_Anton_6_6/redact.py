import sys
import os


def redact(line_num, value):
    with open('bakery.csv', 'r+', encoding='utf-8') as file:
        temp_file = open('bakery_temp.csv', 'w+')
        operation = 0
        for i, line in enumerate(file, 1):
            if i == int(line_num):
                operation = 1
                temp_file.write(str(value) + '\n')
            else:
                temp_file.write(line)
        if operation == 0:
            print('no such line')
        temp_file.close()
    with open('bakery_temp.csv', 'r', encoding='utf-8') as f1,\
            open('bakery.csv', 'w', encoding='utf-8') as f2:
        f2.write(f1.read())
    os.remove('bakery_temp.csv')


redact(sys.argv[1], sys.argv[2])
