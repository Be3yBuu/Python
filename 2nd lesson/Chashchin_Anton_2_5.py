prices = [57.8, 46.51, 97, 76.1, 15.8, 42, 103.1, 72.4, 44, 71.7, 23.5, 17.1]
price_string = ''
# A. one string of prices:
for i in prices:
    rub = int(i)
    penny = (i - rub) * 100
    price_string += f"{rub} рублей {penny:02.0f} копеек "

print(price_string)

# B. sorted list of prices:
for i in sorted(prices, key=float):
    rub = int(i)
    penny = (i - rub) * 100
    print(f"{rub} рублей {penny:02.0f} копеек ")

# C. sorted list of prices desc:
for i in sorted(prices, key=float, reverse=True):
    rub = int(i)
    penny = (i - rub) * 100
    print(f"{rub} рублей {penny:02.0f} копеек ")

# D. five most expensive:
final_list = []
for i in range(5):
    final_list.append((sorted(prices, key=float, reverse=True)[i]))
for i in range(4, -1, -1):
    print(final_list[i])
