# Some more function/precaution in decorator\
def decorator_function(any_function):
    def wrapper_function(*args, **kwargs):    # We should write *args, **kwargs
        print('This is awesome function')
        return any_function(*args, **kwargs)    # 1. We should write return whether the function return or printing the value
                                 # 2. Same we should write *args and **kwargs
    return wrapper_function

# Example 1 with one argument with printing value 
@decorator_function
def func(a):    #this function take one argument
    print(f'This is function with argument {a}')

func(4)


# Example 2 with returning values
# @decorator_function
def add(a, b):
    return a+b

add = decorator_function(add)
print(add(2,3))