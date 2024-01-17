from pdb import set_trace    # Import pdb module (Python Debugger)
# Module - python file contain usefull classes and fucntion wrote by developer

# According to wikipedia - Debugging is the process of finding and resolving 
# defects or problems within in a computer program that prevent correct operation of computer software or a system

# Why debugging
# 1. Our program is not running and causing unexpected errors.
# 2. Our program is working fine but not working the same way we want.

# Steps for debugging
# 1. set_trace() func
# 2. Execute code line by line
        # By the mean of line by line debugging. we need to commentout all the code ad check one by one line


# Now debug this code and see the problem
# set_trace()    # Python debugger
name = input("Enter your name : ")
age = input("Enter your age : ")
print(f"Your name is {name} and your age is {age}")
age = int(age) + 5    # Now we found the problem. We took the int input in the string :/
print(f"After 5 years you will be {age} years old")


# Basic Commands
# l - For check line
# n - for next execution (Important)
# c - for exiting
# q - also for exiting (quiting)