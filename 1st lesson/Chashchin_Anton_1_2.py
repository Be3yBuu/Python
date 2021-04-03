def sum_of_list(number):
    list_sum_var = 0
    while number > 0:
        digit = number % 10
        list_sum_var += digit
        number = number // 10
    return list_sum_var


sqr_lst = []

for n in range(1, 1000):
    list_sum = 0
    if n % 2 == 1:
        sqr_n = n ** 3
        if sum_of_list(sqr_n) % 7 == 0:
            sqr_lst.append(sqr_n)

print(sum(sqr_lst))

for n in range(len(sqr_lst)-1, -1, -1):
    sqr_lst[n] += 17
    if sum_of_list(sqr_lst[n]) % 7 != 0:
        del sqr_lst[n]

print(sum(sqr_lst))
