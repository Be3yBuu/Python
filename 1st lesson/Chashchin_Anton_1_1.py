time = (
    ('year', 31536000),
    ('month', 2628000),  # 365*86400/12
    ('day', 86400),
    ('час', 3600),
    ('мин', 60),
    ('сек', 1)
)


def display_time(sec):
    result = []
    for name, count in time:
        var = sec // count
        if var:
            sec -= var * count
            result.append("{} {}".format(var, name))
    return ' '.join(result) + ';'


print(display_time(99999999))
