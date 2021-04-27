from itertools import islice
# islice не хочет возвращать полный список строк файла, возврает через 1 строку.
# Причем любые другие (кроме csv файлов) итерируемые объекты он возвращает полностью
# пример того, как я хотел начать решать:
users = open('users.csv')
hobby = open('hobby.csv')
for i in range(sum(1 for i in users)):
    with open('users_hobby.txt', 'a', encoding='utf-8') as f_txt:
        f_txt.write(*islice(users, i, i + 1))   # тут, так как он не видит некоторые строки, он начинает ошибки сыпать
hobby.close()
users.close()
