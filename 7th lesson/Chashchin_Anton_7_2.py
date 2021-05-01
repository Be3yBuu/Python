import os
import yaml

#   Папка - dict, значением которого является list (может быть пустым)
#   Файл - str объект
#   Чуть позже понял, что можно было не dict на папку выделять, а list, где первый элемент - название.
#   Не стал переделывать

my_project = [
    {'my_project': [
        {'settings':
             ['__init__.py', 'dev.py', 'prod.py']},
        {'mainapp': ['__init__.py', 'models.py', 'views.py',
                     {'templates': [{'mainapp': ['base.html', 'index.html']}]}]},
        {'authapp': ['__init__.py', 'models.py', 'views.py',
                     {'templates': [{'authapp': ['base.html', 'index.html']}]}]},
        {'empty.folder': []}
    ]}
]
yaml_file = open('config.yaml', 'w')
yaml_file.write(yaml.dump(my_project))
yaml_file.close()
directory = os.path.abspath(os.getcwd())

with open('config.yaml') as y_f:
    file_structure = yaml.safe_load(y_f)


def make_structure(structure):
    global directory
    for item in structure:
        if type(item) is str:
            str_dir = os.path.join(directory, item)
            file = open(str_dir, 'w')
            file.close()
            if len(structure) != 1 and structure[-1] == item or len(structure) == 1:
                directory = '\\'.join(directory.split('\\')[:-1])
        elif type(item) is list:
            if len(item) != 0:
                make_structure(item)
            else:
                directory = '\\'.join(directory.split('\\')[:-1])
        elif type(item) is dict:
            for i in item:
                if not os.path.exists(os.path.join(directory, i)):
                    os.mkdir(os.path.join(directory, i))
                directory = directory + "\\" + str(i)
                make_structure(item.values())
                *_, last = structure
                if last == item:
                    directory = '\\'.join(directory.split('\\')[:-1])
        else:
            raise SyntaxError('неопознанный формат в структуре')


make_structure(file_structure)
