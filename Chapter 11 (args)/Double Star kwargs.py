# **kwargs (Keyword Argument)
# **kwargs Double Star Operator 

# Example 1.
def func(**kwargs):
    """Take Input as a Dictionary"""
    print(kwargs)
    print(type(kwargs))

# func(firs_name='Abbas', last_name='Ali')



# Example 2. (With Normal Parameter)
def func_1(name, **kwargs):
    print(kwargs)
    print(name)

# func_1('Abbas', first_name='Abbas', last_name='Ali')


# Example 3. Unpacking
def func_2(**kwargs):
    print(kwargs)


dic = {'first_name' : 'Abbas', 'last_name' : 'Ali'}
# func_2(**dic)


# Example 4. (Loop)
def func_3(**kwargs):
    for i,j in kwargs.items():
        print(f"{i} : {j}")

print(func_3( first_name='Abbas', last_name='Ali', full_name='Abbas Ali'))
