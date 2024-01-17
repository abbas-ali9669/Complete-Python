# Intor to Decorator (Most Impoortant topic)
# First you have to have a complete understanding of functions
# First class functions/closures
# Then finally we will learn about Decorators

# Example
def square(a):
    return a**2

s = square
print(s(5))    # We can also don this. the both s var and sqaure is same.

print(s.__name__)
print(square.__name__)    # Both are the same

print(s)
print(square)    # Both are the same position in the memory. cause the bith are same

