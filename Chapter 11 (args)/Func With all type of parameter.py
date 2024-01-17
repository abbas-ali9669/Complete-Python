# Function With All Type Of Parameter
# Very Important to understand

# NOTE - Usefull Metohd for memorizing is (PADK)

# Parameter
# *args
# Defaut Parameter
# **kwargs

# Example
def all_func(name, *args, last_name='Ali', **kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)

all_func('abbas', 1,2,3,4, a=1, b=2)


# Defaul Parameter
def default(first_name='Abbas', last_name='Ali'):
    print(first_name)
    print(last_name)

default()