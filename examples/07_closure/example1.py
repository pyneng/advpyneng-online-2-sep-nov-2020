def multiply(num1):
    print("Вызываю multiply")
    list_var = [1, 2, 3]
    string = "test"
    def inner(num2):
        print("Вызываю inner")
        return num1 * num2
    return inner
