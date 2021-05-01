import re


def email_parse(email_address):
    parse = re.findall(r'^[a-z1-9]+@[a-z1-9]+\.[a-z1-9]+$', email_address, re.IGNORECASE)
    if parse:
        parse_split = re.split(r'@', email_address)
        return {'username': parse_split[0], 'domain': parse_split[1]}
    else:
        raise ValueError('wrong email' + email_address)


print(email_parse('d123dsFg@sdf12.ru'))
# re.split тут будет лучше, чем re.compile(), в виду сокращения кол-ва необходимых операций
