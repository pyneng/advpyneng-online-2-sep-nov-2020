from functools import wraps


def all_numbers(func):
    print("Вызываю декоратор")
    @wraps(func)
    def inner(*args):
        if not all([isinstance(arg, int) for arg in args]):
            raise ValueError(f"Все аргументы должны быть int")
        return func(*args)
    return inner


def force_arg_type(required_type):
    print("Вызываю force_arg_type")
    def decorator(func):
        print("Вызываю декоратор")
        @wraps(func)
        def inner(*args):
            if not all([isinstance(arg, required_type) for arg in args]):
                raise ValueError(f"Все аргументы должны быть "
                                 f"{required_type.__name__}")
            return func(*args)
        return inner
    return decorator

all_numbers = force_arg_type(int)
all_str = force_arg_type(str)



@force_arg_type(int)
def summ(a, b):
    return a + b


decorator = force_arg_type(int)
summ = decorator(summ)

