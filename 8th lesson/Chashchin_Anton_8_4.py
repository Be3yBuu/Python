def val_checker(lamb):
    def positive(func):
        def wrapper(*args):
            result = func(*args)
            if not lamb(*args):
                raise ValueError('wrong val ' + str(args[0]))
            return result

        return wrapper

    return positive


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


print(calc_cube(5))
print(calc_cube(-5))

