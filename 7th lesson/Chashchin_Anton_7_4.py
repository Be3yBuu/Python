import os

folder_path = r'E:\download'
files = []
file_len_dict = {}
try:
    for r, p, f in os.walk(folder_path):
        for i in f:
            files.append(os.stat(folder_path + '\\' + i).st_size)
except OSError:
    pass

for i in files:
    if 10 ** len(str(i)) in file_len_dict:
        file_len_dict[10 ** len(str(i))] = file_len_dict[10 ** len(str(i))] + 1
    else:
        file_len_dict[10 ** len(str(i))] = 1

sorted_file_dict = sorted(file_len_dict.items())

x = ({num: val} for num, val in sorted_file_dict)
print(*x)
