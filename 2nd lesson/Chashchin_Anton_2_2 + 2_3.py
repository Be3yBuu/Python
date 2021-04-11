sentence = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
int_digit_list = []
number_string = 0

for idx, string in enumerate(sentence):
    digit_count = 0
    for i in range(len(string)-1, -1, -1):
        if i == len(string)-1:
            if string[i:].isdigit():
                digit_count += 1
                number_string = i
                int_digit_list.append(idx)
            if digit_count % 2 == 1 and (i % 2 == 0 or i == 0):
                digit_count = 0
                sentence[idx] = '0' + string[number_string:]

        else:
            if string[i:i+1].isdigit():
                digit_count += 1
                number_string = i
                int_digit_list.append(idx)
            if digit_count % 2 == 1 and (i % 2 == 0 or i == 0):
                sentence[idx] = string[:number_string] + '0' + string[number_string:]
                string = sentence[idx]
                digit_count = 0

print(sentence)

for i in range(len(sentence)-1, -1, -1):
    if i in set(int_digit_list):
        sentence.insert(i+1, '"')
        sentence.insert(i, '"')
print(sentence)

# reverse to put '"' w/o spaces
for idx, list_str in enumerate(sentence):
    if list_str == '"':
        del sentence[idx]

for i in range(len(sentence)-1, -1, -1):
    if i in set(int_digit_list):
        sentence[i] = '"' + sentence[i] + '"'
print(' '.join(sentence))
