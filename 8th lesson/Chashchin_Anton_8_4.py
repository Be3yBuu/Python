def val_checker():
    def positive(func):
        def wrapper(*args):
            result = func(*args)
            if args[0] < 0:
                raise ValueError('wrong val ' + str(args[0]))
            return result

        return wrapper

    return positive


@val_checker()
def calc_cube(x):
    return x ** 3


print(calc_cube(5))
print(calc_cube(-5))
