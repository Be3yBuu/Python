from itertools import zip_longest


def zip_tut_klass():
    if len(tutors) <= len(klasses):
        tuple_var = zip(tutors, klasses)
    else:
        tuple_var = zip_longest(tutors, klasses)
    for tut_class_name in tuple_var:
        yield tut_class_name


tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']
class_len = len(list(zip_tut_klass()))
class_names = zip_tut_klass()
for _ in range(class_len):
    print(next(class_names))
