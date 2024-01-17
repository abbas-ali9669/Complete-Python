# Important Summary 
# 1. *args
def func_1(*args):    #take input as a Tuple
    total = 0
    for i in args:
        total += i
    return total

# print(func_1(1,2,3,4))


# ---> *args with normal parameter
def func_2(name, *args):
    total = 0
    for a in args:
        total += a
    return (f"{total}\n{name}")  #String Formating

# print(func_2('Abbas Ali', 1,2,3,4))


# ---> *args as Arguments
def func_3(*args):
    total = 0
    for i in args:
        total += i
    return total

num = 1,2,3,4
# print(func_3(*num))    # Unpacking


# 2. **kwargs()
def func_4(**kwargs):
    # return (kwargs)    #take input as a Dictionary
    for i, j in kwargs.items():
        print(f"{i} : {j}")

# func_4(name='Abbas', age=21)

# ---> **kwargs with normal parameter 
def func_5(name, **kwargs):
    print(name)
    print(kwargs)

# func_5('Abbas Ali', names='abbas', age=21)

# ---> **kwargs as argument
def func_6(**kwargs):
    return kwargs

dic = {'name' : 'abbas', 'age' : 21}    # Unpacking
# print(func_6(**dic))


# 3. function with all type of parameter
# Techniques ---> PADK (Noraml Parameter, *args, Default Parameter, **kwargs)
def func_7(first_name, *args, last_name='Ali', **kwargs):
    print(first_name)
    total = 0
    for i in args:
        total += i
    print(total)
    print(last_name)
    print(kwargs)

# func_7('Abbas', 1,2,3,4, nams='Abbas', age=21)

################################# THE END #######################################