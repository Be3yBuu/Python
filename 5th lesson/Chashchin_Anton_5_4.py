def higher_num_gen():
    higher = []
    for i in range(1, len(src) - 1):
        if src[i] > src[i - 1]:
            higher.append(src[i])
    for i in higher:
        yield i


src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(list(higher_num_gen()))
