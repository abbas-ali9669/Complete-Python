# define a decorator that print the following func line
# 1. You are calling {} func
# 2. the doc string of func
# 3. the output of func
from functools import wraps
def print_func_data(any_func):
    @wraps(any_func)
    def wrapper_func(*args, **kwargs):
        print(f"You are calling {any_func.__name__} function")
        print(any_func.__doc__)
        return any_func(*args, **kwargs)
    return wrapper_func


@print_func_data
def add(a, b):
    ''' this func take two argument and return their sum '''
    return a+b

print(add(2,2))


# func = print_func_data(add)
# print(func(2,2))
