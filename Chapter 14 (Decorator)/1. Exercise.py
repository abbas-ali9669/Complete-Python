# In this exercise we will calculate the total time of our func that how much time our func is take to execute
# for time calculating we use time module

# Solution
import time
from functools import wraps

def calculate_time(any_func):
    @wraps(any_func)
    def wrapper_func(*args, **kwargs):
        print(f"Executing... \"{any_func.__name__}\" Function")
        t1 = time.time()
        returned_value = any_func(*args, **kwargs)
        t2 = time.time()
        total_time = t2-t1
        print(f"This func take {total_time} in execution")
        return returned_value
    return wrapper_func

@calculate_time
def square(n):
    new = []
    for i in range(1, n+1):
        new.append(i**2)
    return new

square(10)

