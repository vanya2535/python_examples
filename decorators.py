def my_decorator(func):
    def wrapper(x, y):
        x += y
        return func(x, y)

    return wrapper


@my_decorator
def func(x, y):
    return x + y


print(func(1, 2))
