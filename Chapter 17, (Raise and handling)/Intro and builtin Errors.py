# Today we will discuss about Builtin errors 
# Which error that what means of errors

# 1. Syntax Error: Miss the coerrect method of writing code
# Example
def func:
    pass


# 2. Indentation Error: Occurs when we skip the spaces from the block function
def func():
    print("Hello")
   print("World")    # Indentation Error


# 3. Name Error: Occurs when did not declare the variable the we run the name without defining the variable
print(name)    # Name error


# 4. Type Error: Occur when we input the wrong datatype
print(5 + "Abbas")    # TypeError because string cannot add with integer
print(5 * "Abbas")    # But we can do this


# 5. Index Error: Occur when we input the wrong index. and the index is doesn't exist
l = [1,2,3]
print(l[4])


# 6. Value Error: Occur When you put the correct datatype but the wrong value
n = "abc"
print(int(n))    # Value Error


# 7. Attribute Error: Occur when we use the function that doesn't exist
l = [1,2,3]
l.push()    # Attribute Error: The push function is not defined


# 8. Key Error: Occur when the key is not exist in dictionary
d = {"name": "Abbas"}
print(d['age'])    # Key Error the key age is not defined

