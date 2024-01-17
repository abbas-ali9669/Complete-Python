# In this topic we will discuss about raise error means we will make our own error in this topic
# Example
def add(a,b):
    if (type(a) is int) and (type(a) == int):
        return a+b
    raise TypeError("Wrong DataType")

print(add(2,2))
# Q - Why this is imortant
# A - Besause if we do nor raise our error the return value of the will store to application dataase. which we don't want
