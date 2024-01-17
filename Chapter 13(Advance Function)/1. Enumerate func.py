# Enumerate Function.
# We use enumerate fncyion with for loop to track position of our item in iterable.

items = ['abc', 'xyz', 'abbas', 'ali']


# 1. Without enumerate function.
pos = 0
for i in items:
    print(f"{pos} ---> {i}")
    pos += 1


# 2. With enumerate function
for pos, i in enumerate(items):
    print(f"{pos} ---> {i}")



# Simple Exercise
# define a function that take two arguments
# 1.) List containing string
# 2.) String that want to find in your list
# and this function will return the index of string in your list and 
# if string is not present then return -1
# For finding specific item index
def filter(l, target):
    for pos, i in enumerate(l):
        if i == target:
            return pos
    return -1

print(filter(items, 'abbas'))

# Method 2
l = [50, 60, 40, 70, 90, 30, 100]
for i in range(len(l)):
    if l[i] == 40:
        print(i)

# With while loop
i = 0
while i < len(l):
    if l[i] == 40:
        print(i)
    i += 1