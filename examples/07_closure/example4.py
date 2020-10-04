def operations(num1, num2):
    def add():
        return num1 + num2

    def sub():
        return num1 - num2

    def mul():
        return num1 * num2

    operations.add_num = add
    operations.sub_num = sub
    operations.mul_num = mul

    return operations
