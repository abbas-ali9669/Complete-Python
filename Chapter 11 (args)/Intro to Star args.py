# Star(*) args 
# Make Flexible Function

# Name - *args or *operator

# Example 
def total(a,b):
    return a+b

print(total(2,2))


# 2.
def all_total(*args):
    print(args)
    print(type(args))

all_total(1,2,3,4,5)


# Main Method
# Easy way to sum the number
def total_(*args):
    total = 0
    for i in args:
        total += i
    return total

print(total_(1,2,3,))


# Example (Multiply)
def multiply_nums(*args):
    multiply = 1
    for i in args:
        multiply *= i
    return multiply

# print(multiply_nums(1,2,3))