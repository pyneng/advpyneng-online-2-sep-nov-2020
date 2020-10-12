from datetime import datetime
import time


class MegaDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start = datetime.now()
        print("__call__")
        result = self.func(*args, **kwargs)
        time.sleep(1)
        print(f"Время работы {datetime.now() - start}")
        return result



#@MegaDecorator
def upper(string):
    return string.upper()


upper = MegaDecorator(upper)
