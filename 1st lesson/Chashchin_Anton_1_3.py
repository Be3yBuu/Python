text_list = [' процент', ' процента', ' процентов']


def percent(var):
    if var == 0 or var > 4:
        text_list_var = 2
    elif var == 1:
        text_list_var = 0
    else:
        text_list_var = 1
    print(str(var) + text_list[text_list_var])


percent_input = int(input('Введите число: '))

percent(percent_input)

for i in range(0, 20):
    percent(i)