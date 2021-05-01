import re
# на мой взгляд - самое логичное решение:

file = open('nginx_logs.txt')

for line in file:
    parse = re.split(r'\ /| "|]|\[|\ ', line)

    parsed_raw = (parse[0], parse[4] + ' ' + parse[5], parse[7], parse[8], parse[10], parse[11])

    print(parsed_raw)
file.close()

# если нужно парсинг одной строки, и как показано в примере:

raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-"' \
      ' "Debian APT-HTTP/1.3 (0.9.7.9)"'
parsed_raw = (
    re.search(r'(?:\d{1,3}\.){3}\d{1,3}', raw).group(),
    re.search(r'\d{1,2}/\w+/\d{1,4}(?::\d{2}){3}\ \+\d{4}', raw).group(),
    re.search(r'(?:"[A-Z]+)', raw).group().strip('"'),
    re.findall(r'(?:/.*?){2}\ ', raw)[1],
    re.findall(r'\ [0-9]+', raw)[0],
    re.findall(r'\ [0-9]+', raw)[1],
)
print(parsed_raw)

# можно конечно было написать в одну строку через |, но надо намного точнее знать что есть, кроме GET функции,
# какие папки есть, из которых берутся файлы и так далее.
