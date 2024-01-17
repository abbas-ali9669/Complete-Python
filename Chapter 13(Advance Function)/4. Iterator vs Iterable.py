# Iterator vs Iterables
# NOTE - list, Tuple, String all are Iterables

num = [1,2,3,4,5]    #Iterable
squares = map(lambda a: a**2, num)    #Iterator
# for iterator we don need to use iter func() we can directly apply next func()
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))

# Q - How for loop works
# A - 
# 1. For loop calls the iter func()
num_iter = iter(num)
print(type(num_iter))
# 2. Then iter function calls the next func() for value changing
print(next(num_iter))
print(next(num_iter))
print(next(num_iter))
print(next(num_iter))
print(next(num_iter))

