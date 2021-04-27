file = open('nginx_logs.txt')
ip_dict = {}
for line in file:
    ip = line.split(' ')[0]
    ip_dict.setdefault(ip, 0)
    ip_dict[ip] = ip_dict[ip] + 1

file.close()

flood_ip = ''
max_spam = 0
for key in ip_dict:
    if ip_dict[key] > max_spam:
        max_spam = ip_dict[key]
        flood_ip = key
print(flood_ip, max_spam)
