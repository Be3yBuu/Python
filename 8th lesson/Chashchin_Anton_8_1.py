import re


def email_parse(email_address):
    parse = re.search(r'^[a-z1-9]+@[a-z1-9]+\.[a-z1-9]+$', email_address, re.IGNORECASE)
    if parse:
        parse_split = re.split(r'@', email_address)
        return {'username': parse_split[0], 'domain': parse_split[1]}
    else:
        raise ValueError('wrong email ' + email_address)


print(email_parse('d123dsFg@sdf12.ru'))
# я считаю, что re.compile тут не нужен, мы всё равно проверяем целую строку на наличие в ней шаблона, от ^ до $
