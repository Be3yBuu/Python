import os
import shutil

my_folder = os.path.abspath(os.getcwd())
file_paths = []

for abs_adr, folders, files in os.walk(my_folder):
    for idk in files:
        if '.html' in idk:
            if abs_adr not in file_paths:
                file_paths.append(abs_adr)
if not os.path.exists(os.path.join(my_folder, 'my_project\\templates')):
    os.mkdir('my_project\\templates')
else:   # опустошаем папку templates перед её заполнением
    for adr, folders, files in os.walk('my_project\\templates'):
        for i in files:
            os.unlink(os.path.join(adr, i))
        for i in folders:
            shutil.rmtree(os.path.join(adr, i))
for i in file_paths:
    dirs = os.path.join(my_folder, os.path.dirname(i))
    shutil.copytree(i, 'my_project\\templates\\' + i.split('\\')[-1])
