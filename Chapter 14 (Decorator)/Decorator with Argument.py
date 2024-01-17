# Decorator with argument 
from functools import wraps
def only_data_type(data1, data2):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            if all([type(i) == data1 or type(i) == data2 for i in args]):
                return function(*args, **kwargs)
            return "Wrong Input"
        return wrapper
    return decorator


@only_data_type(int, None)    # Here we can put aur data type 
def additon(*args):
    total = 0
    for i in args:
        total += i
    return total

print(additon(1,2,3,4,5,))


@only_data_type(list, tuple)
def sqaure(a):
    new = []
    for i in a:
        new.append(i**2)
    return new

print(sqaure([1,2,3,4,5,6,7,8,9,10]))
print(sqaure((1,2,3,4,5,6,7,8,9,10)))