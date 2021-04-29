import os
import json

folder_path = r'E:\download'
files = []
file_len_dict = {}
not_read = 0
try:
    for r, p, f in os.walk(folder_path):
        for i in f:
            files.append({os.stat(folder_path + '\\' + i).st_size: i.split('.')[-1]})
except OSError:
    not_read += 1
    pass
for i in files:
    for key, value in i.items():
        if 10 ** len(str(key)) in file_len_dict:
            file_len_dict[10 ** len(str(key))][0] = file_len_dict[10 ** len(str(key))][0] + 1
            if value not in file_len_dict[10 ** len(str(key))][1]:
                file_len_dict[10 ** len(str(key))][1].append(value)
        else:
            file_len_dict[10 ** len(str(key))] = [1, []]
for i in file_len_dict:
    file_len_dict[i] = tuple(file_len_dict[i])  # Смысл от этого, если json их всё равно в list превратит?
print(file_len_dict)

our_folder = os.path.basename(os.path.dirname(os.getcwdb())).decode('utf-8')
with open(f'{our_folder}_summary', 'w', encoding='utf-8') as f_json:
    json.dump(file_len_dict, f_json, ensure_ascii=False)
