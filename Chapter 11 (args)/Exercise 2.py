# Define a Function 
# names = ['abbas', 'bilal']
# that return a first letter of your string capital
# method use 
# print(func(name, reverse_str = True))

# Solution 
def func(l, **kwargs):
    if kwargs.get('reverse_str') == True:
        return [name[::-1].title() for name in l]
    else:
        return [name.title() for name in l]


names = ['abbas', 'bilal']
# print(func(names, reverse_str = True ))


print(names.title())


# Method 2
def func(l, **kwargs):
    new = [name[::-1] if kwargs.get('reverse_str') == True else name.title() for name in l]
    return new

l = ['abbas', 'bilal']
print(func(l,))