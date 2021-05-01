from functools import wraps


def type_logger(func):
    @wraps(func)
    def logging(log_type):
        return str(calc_cube.__name__) + '(' + str(log_type) + ': ' + str(type(log_type)) + ')'

    return logging


@type_logger
def calc_cube(nothing):
    return nothing ** 3


print(calc_cube(5))
