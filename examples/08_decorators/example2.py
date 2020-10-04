from functools import wraps


def verbose(func):
    print("Вызываю декоратор verbose")

    @wraps(func)
    def inner(*args, **kwargs):
        print(f"У функции {func.__name__} такие аргументы {','.join(map(str, args))}")
        return func(*args, **kwargs)

    return inner


def all_numbers(func):
    print("Вызываю декоратор all_numbers")

    @wraps(func)
    def inner(*args):
        if not all([isinstance(arg, (int, float)) for arg in args]):
            raise ValueError("Все аргументы должны быть числами")
        return func(*args)

    return inner


@verbose
@all_numbers
def add(num1, num2):
    return num1 + num2


# add = verbose(all_numbers(add))


@all_numbers
def sub(num1, num2):
    return num1 - num2


@all_numbers
def mul(num1, num2):
    return num1 * num2
