# write our first generator 
# there are two method to write our generator
# 1. Generator Function
# 2. Generator Comprehension


# 1. Generator function
# Write a code to generate number to n
def num(n):
    for i in range(1, n+1):
        # print(i)    # Normal method
        yield i    # Generator function

number = num(10)    # Now here we generate our sequence in object. Now we can iterate it once
# print(number)    # This will ask for object 

# These loops are runs only once 
for i in number:
    print(i)

for j in number:
    print(j)


# NOTE - The generator will print only one we can use only one iteration over generator
# but one more method we can generate a sequence many time 
# is to generate a sequence in loop
for i in num(10):
    print(i)

for j in num(10):
    print(j)

# NOTE - if we generate our sequence in the object. then we can iterate only once
# otherwise we can generate it in loop many times