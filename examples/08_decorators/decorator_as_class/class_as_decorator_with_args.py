from datetime import datetime
import time


class MegaDecorator:
    def __init__(self, message):
        self.msg = message

    def __call__(self, func):

        def inner(*args, **kwargs):
            start = datetime.now()
            print(self.msg)
            print("__call__")
            result = func(*args, **kwargs)
            time.sleep(1)
            print(f"Время работы {datetime.now() - start}")
            return result
        return inner



@MegaDecorator("hello")
def upper(string):
    return string.upper()

