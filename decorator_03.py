def type_logger(func):

    def wrapper(*args):
        calc = func(*args)
        for i in range(len(args)):
            print(f'{args[i]}: {type(args[i])}')
        return calc

    return wrapper


@type_logger
def calc_cube(x, *args):
    return x ** 3


test = calc_cube(5, 15, 12)
print(test)
