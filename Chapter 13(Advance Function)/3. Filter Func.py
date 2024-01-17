# Filter() Function
# Filter the number from our object and return the value
num = [2,1,3,4,5,6,7,8,9,10]

# With def func()
def even(a):
    return a%2 == 0


evens = list(filter(even, num))
print(evens)

# with lambda (filter)
new_even = filter(lambda a: a%2==0, num)
print(list(new_even))


# with LC 
new_even2 = [i for i in num if (i%2 == 0)]
print(new_even2)


# default Method
def new_even3():
    new = []
    for i in range(1,11):
        if i%2 == 0:
            new.append(i)
    return new

print(new_even3())