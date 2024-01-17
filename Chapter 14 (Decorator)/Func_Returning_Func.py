# Example 1.
def outer_func():
    def inner_func():
        print("This is inner function")
    return inner_func    # We can also use this method for calling (return inner_func())

var = outer_func()    # When the outer return the inner func the variable store the value of inner func
var()



# Example 2
def outer_func_2(message):
    def inner_func_2():
        print(f"The messsage is {message}")
    return inner_func_2()

var_2 = outer_func_2('Hello There !')
var_2