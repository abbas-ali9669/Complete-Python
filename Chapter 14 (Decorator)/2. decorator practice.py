from functools import wraps
# There is some problem with with reading the doc string of function
def decorator_func(any_func):
    @wraps(any_func)
    def wrapper_func(*args, **kwargs):
        """ This is wrapper function """
        print("This function is awesome")
        return any_func(*args, **kwargs)
    return wrapper_func


@decorator_func
def add(a, b):
    """ this is add function """
    return a+b

print(add(2,3))
# now if we want to read the doc string of add func
print(add.__doc__)    #this will print the wrapper doc string because this is wrapper_func
print(add.__name__)    #this will print wrapper func]

# NOTE - now here we have to import the modules name (functools)
print(add.__doc__)    # Now this will work properlyafter importing module
print(add.__name__)

