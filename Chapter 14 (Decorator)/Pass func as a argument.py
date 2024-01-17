# In this func we will pass our function as a argument 
# means we will create our own function like map() function

# Old Example
l = [1,2,3,4,5]

def square(a):
    return a**2

# print(list(map(square, l)))    # Works Properly

# Now we will make our own function like map
def my_map(func, l):
    new_list = []
    for item in l:
        new_list.append(func(item))
    return new_list

print(my_map(square, l))   # We have created our pwn function like map
print(my_map(lambda a: a**2, l))   # We can also use here lambda expression


# With list comprehension
def my_map_2(func, l):
    return [func(item) for item in l]

print(my_map_2(square, l))    # This to works properly
print(my_map_2(lambda a: a**2 , l))    # Same we can use lambda 