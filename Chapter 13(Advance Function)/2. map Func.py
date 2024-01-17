# MAP Function
# Example
# Q - When to use map() function
# A - When use pre-defined (len, int, float, etc) then use map. otherwise LC or other
number = [1,2,3,4]
def square(a):
    return a**2

# print([square(2), square(3), square(4)])    #Too Long

# With map func()
squares = list(map(lambda a: a**2, number))
print(squares)


# with list Comprehension
square2 = [i**2 for i in number]
print(square2)

# Without List Comprehension
new_list = []
for i in number:
    new_list.append(square(i))
print(new_list)

# predefined function with map function
mixed = ['abc', 'xyz', 'lmn', 'Abbas']
lenght = list(map(len, mixed))
print(lenght)

# Map function is iterable
for i in lenght:
    print(i)