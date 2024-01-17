# Practice with lambda expression
# Example (even number) More shorter code
# ---> Noraml Code
def even(e):
    if e%2 == 0:
        return True
    return False

# print(even(2))

# ---> More Shorter
def even_1(e):
    return e%2 == 0

# print(even_1(2))

# ---> With lmabda
even_2 = lambda e : e%2 == 0
# print(even_2(2))


# Example 2 (Last Char)
def last_alph(l):
    return l[0]

# print(last_alph('abbbas'))

# With lambda 
last_alph_1 = lambda l : l[0]
# print(last_alph_1('abbas'))


# Example 3 lenght  (if, else with lambda)
def lenght_(s):
    if len(s) > 5:
        return True
    return False

# print(lenght_('abb'))

# More Shorter 
def lenght_1(s):
    return len(s) > 5

# print(lenght_1('abbas ali'))

# With lambda 
lenght_2 = lambda s : True if len(s) > 5 else False
# print(lenght_2('abbas ali'))

# More Shorter
lenght_3 = lambda s : len(s) > 5
print(lenght_3('Abbas ALi'))

