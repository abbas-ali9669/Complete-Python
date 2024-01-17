# Finally with Decorator 
# Decorator is use to inhance/increase the functionality of other function
#  without changing the function code

# Example
# How to define decorator
def decorator_func(any_func):    # This func will one func as input
    def wrapper_func():
        print("This is awesome function")
        any_func()    # Here we call our function
    return wrapper_func




# Func 1
def func1():
    print('This is function 1')

# Func 2
def func2():
    print('This is function 2')


# func1()
# func2()    #This method will print the func

# how to use decorator
# With func 1
func1 = decorator_func(func1)    # Here we call our decorator and pass our function
func1()

# With func 2
func2 = decorator_func(func2)
func2

# decorator with Shortcut (@)
# With the use of this your function will runn corractly too
@ decorator_func
def func3():
    """ This function uses Decorator """
    print("This is function 3")


func3()
print(func3.__doc__)