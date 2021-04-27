import csv
import itertools
import json
hobby = open('hobby.csv')
users = open('users.csv')
hobby_reader = csv.reader(hobby, delimiter=' ')
users_reader = csv.reader(users, delimiter=' ')
hobby_list = []
users_list = []
for row in hobby_reader:
    hobby_list.append(row[0])
for row in users_reader:
    users_list.append(row[0])
if len(hobby_list) < len(users_list):
    with open('file.json', 'w', encoding='utf-8') as f_json:
        json.dump({line1: line2 for line1, line2 in itertools.zip_longest(users_list, hobby_list)}, f_json,
                  ensure_ascii=False)
else:
    with open('file.json', 'w', encoding='utf-8') as f_json:
        json.dump({line1: line2 for line1, line2 in zip(users_list, hobby_list)}, f_json, ensure_ascii=False)
    print('1')  # не понял фразу "выходим из скрипта с кодом '1'"
hobby.close()
users.close()
