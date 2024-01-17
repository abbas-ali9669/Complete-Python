# __doc__ string
# NOTE - doc string is use for help that what the function will do
# Example
def add(a,b):
    '''This func take two argument and return the sum of argument'''
    return a+b

print(add(2,3))
# For viewing doc string of any function
print(add.__doc__)

# To see any func doc string like (len, min, max, sum, sorted)
print(len.__doc__)
print(sorted.__doc__)


# 2. If you dont know about any func that what this function will do use help func
print(help(sum))
print(help(len))