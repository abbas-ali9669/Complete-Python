# NOTE - When you use *args as a argument you have to use * to unpack the list, tuple
def multiply_nums(*args):
    multiply = 1
    for i in args:
        multiply *= i
    return multiply

num = (2,3,4)
print(multiply_nums(*num))    #Unpacking *args as a arguments

