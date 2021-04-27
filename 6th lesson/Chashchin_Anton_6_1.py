file = open('nginx_logs.txt')
for line in file:
    result = [line.split(' ')[0], line.split(' ')[5][1:], line.split(' ')[6]]
    print(tuple(result))
file.close()
