from functools import wraps
def decorator(fun):
    @wraps(fun)
    def wrapper(*args, **kwargs):
        if all([type(arg) == int or type(arg) == float for arg in args]):
            return fun(*args, **kwargs)
        return "Invalid Input"
    return wrapper


