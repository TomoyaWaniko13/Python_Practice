def function_decorator(function):
    def decorated_function():
        print('****')
        function()
        print('****')
        print()
    return decorated_function()


@function_decorator
def hello():
    print('hello')


@function_decorator
def bye():
    print('see you!')

a = function_decorator(hello)