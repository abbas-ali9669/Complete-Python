# These type of function is also called Closure or First class function

# Example (Make a func with number and power)
def number(n):
    def power(x):
        return n**x
    return power

cube = number(2)
print(cube(3))

square = number(2)
print(square(2))