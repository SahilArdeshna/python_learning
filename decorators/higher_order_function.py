# Higher Order Function (HOC)
def greet(func):
    return func()


def greet2():
    def func():
        return 1

    return func()
