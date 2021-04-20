def thesaurus_adv(*names):
    name_list = {}
    for name in names:
        if name.split()[1][:1] in name_list.keys():
            if name.split()[0][:1] in name_list[name.split()[1][:1]].keys():
                name_list[name.split()[1][:1]][name.split()[0][:1]].append(name)
            else:
                name_list[name.split()[1][:1]][name.split()[0][:1]] = [name]
        else:
            name_list[name.split()[1][:1]] = {name.split()[0][:1]: [name]}
    return dict(sorted(name_list.items()))


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
