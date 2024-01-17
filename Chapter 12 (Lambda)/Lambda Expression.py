# lambda expression (Anomymous Function)
# lambda has no specific name to define
# we use lambda in some of our function like (map, reduce, filter)

# Example def()
def add(a,b):
    return a+b

# print(add(2,2))    #---> Output = 4
print(add)

# Example (lambda)
# We do not store lmabda in variable
add_2 = lambda a,b : a+b
print(add_2(2,3))
print(add_2)    # It has no name 
