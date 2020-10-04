from functools import wraps

def verbose(func):
    print("Вызываю декоратор verbose")

    @wraps(func)
    def inner(*args, **kwargs):
        print(f"У функции {func.__name__} такие аргументы {','.join(map(str, args))}")
        return func(*args, **kwargs)

    return inner


@verbose # upper = verbose(upper)
def upper(string):
    return string.upper()


@verbose
def lower(string):
    return string.lower()

