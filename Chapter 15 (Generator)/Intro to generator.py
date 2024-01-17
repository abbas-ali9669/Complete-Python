# Intro to generator 
# Generators are iterators
# Q - How generetor works ?
# A - generator work with only one iterable at the same time than other data types

# Q - Why use generator ?
# A - When we wsnt to wokr with only one item 

# Iterator vs iterable

# 1. Iterable
l = [1,2,3,4,5]    # Iterable
# We use loop to make this iterable into iterator
# We cannot use the next() function direct on iterable because the next() function works with iterator
i = iter(l)    # Now this object change into the iteator
# Now We can use next() funcion on because now it becoke iterator
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))

# 2. Iterator
x = map(lambda a : a**2, l)    # This is iterator we can direct use the next() function on it
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))

# We can use loop over map func
for i in map(lambda a: a**2, l):
    print(i)