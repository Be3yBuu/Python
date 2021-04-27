import sys


def read_csv(start=0, stop=0):
    with open('bakery.csv', 'r', encoding='utf-8') as file:
        if len(sys.argv) == 1:
            result = []
            for i in file.readlines():
                result.append(i)
            return ''.join(result)
        elif len(sys.argv) == 2:
            read_list = file.readlines()
            if start != 0:
                return ''.join(read_list[start - 1:]).strip('\n')
            else:
                return ''.join(read_list[start:]).strip('\n')
        else:
            read_list = []
            for i in range(start, stop+1):
                read_list.append(file.readline().strip('\n'))
            return '\n'.join(read_list)


if len(sys.argv) == 2:
    print(read_csv(int(sys.argv[1])))
elif len(sys.argv) > 2:
    print(read_csv(int(sys.argv[1]), int(sys.argv[2])))
else:
    print(read_csv())
