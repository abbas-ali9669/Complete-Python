# *args with normal parameter

# Example (Multiply)
def multiply_nums(*args):
    multiply = 1
    for i in args:
        multiply *= i
    return multiply

# print(multiply_nums(1,2,3))

# With normal parameter
def multiply_nums_2(num, *args):
    multiply = 1
    # print(args)
    # print(num)
    for i in args:
        multiply *= i
    return multiply, num


print(multiply_nums_2(1,2,3))    #The first number is stored in parameter (num) & will not be calculated -
# in *args 
