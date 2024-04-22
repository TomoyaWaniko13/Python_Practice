def hello():
    print('hello')


def my_decorator(func):
    def wrap_func():
        func()

    return wrap_func

@my_decorator
def hello():
    print('hello')

hello()
