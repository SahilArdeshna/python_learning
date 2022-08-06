# Dectorator supercharges a function.
# It simply a function that wraps another function and enhaces it or changes it.


def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print("********")
        func(*args, **kwargs)
        print("********")

    return wrap_func


@my_decorator
def hello(greeting, emoji=":("):
    print(greeting, emoji)


@my_decorator
def greet(greeting):
    print(greeting)


hello("Hellooooo")
# greet("Welcome")
