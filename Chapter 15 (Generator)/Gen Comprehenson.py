# Generator comprehension
# There is simple way to create a generator comprehension

square = (i**2 for i in range(1,11))    # Now the generator creates
print(type(square))
for i in square:
    print(i)
    pass

def gen_comp(n):
    square = (i**2 for i in range(1, n+1))
    return square 

func = gen_comp(10)
for i in func:
    print(i)

# exit()

# 3.
def gen_comp2(n):
    square = (i**2 for i in range(1,n+1))
    print(type(square))
    yield square

# NOTE - if you use generator comprehension and yield keyword in same function 
# then we have to use nested loop for generate a sequence 

func1 = gen_comp2(10)
for i in func1:
    for j in i:
        print(j)

