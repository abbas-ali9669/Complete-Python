def decorator(function):
    def wrapper(*args, **kwargs):
        # With comprehension
        if all([type(arg) == int for arg in args]):
            return function(*args, **kwargs)
        return "Invalid Input"
    return wrapper

    #     type_ = []
    #     for i in args:
    #         type_.append(type(i) == int)
    #     if all(type_):
    #         return function(*args, **kwargs)
    #     return "Invalid input"
    # return wrapper


# For this function we need to inout right int value 
@decorator
def add(*args):
    total = 0
    for i in args:
        total += i
    return total

print(add(1,2,3,4,5,"ewfwf"))    # this will occur errr
# now we need to define the decorator for the right input



# 2. One more method for this function
def addition(*args):
    if all(type(i) == int or type(i) == float for i in args):
        total = 0
        for i in args:
            total += i
        return total
    return "Wrong Input"
    
print(addition(1,2,3, 'ewfwe'))