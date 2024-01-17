# Read file 
# 1. Open function()
# 2. read method
# 3. seek() method
# 4. tell() method 
# 5. readline method
# 6. readlines method
# 7. close() mehtod

# 1. Open Function()\
f = open("file1.txt")    # if we dont write "r" so no problem open func value is by default is on "r" mode


# 2. read() method
# print(f.read())
# This method will read whatever is in our file


# 3. tell mehtod
# print(f"Cursor Position - {f.tell()}\n")
# print(f.read())
# print(f"\nCursor Position - {f.tell()}")
# NOTE - the tell() method will tell us that where is our cursor position before and after the reading
# We cannot read the file twice. Once we read our file the cursor position will on the last. For reading multiple time we use to change the cursor postion to the zero position. For doing this we have the seek() method


# 4. seek() method
# print(f.seek(0))    # Now again our cursor position is on the zeroth position
# print(f.read())
# With the help of seek method we can read our file multiple time by changing the cursor position
# Seek method change the postion of cursor


# 5. readline() method
# This method will read the line one by one
# print(f.readline(), end="")
# print(f.readline(), end="")
# print(f.readline())



# 6. readlines() method
# line = f.readlines()
# this method will give us the list of lines
# We can also iterate this
# for i in line:
#     print(i, end="")

# for i in f.readlines()[0:4]:    # We can tell this how many we want to read
#     print(i)


# 7. close method 
# print(f.closed)    # Checking if file closed or not 

f.close()    # This method is necessary. There is no problem to odnt close your file. But sometimes it create the problem if you dont close the file


# NOTE - There are two discriptive that are used to much. There is no paranthesis at the end of discriptors
# 1. .name: This is for printing the name of our file
# print(f.name)
# 2. .closed: This will tell that our file is closed or not (True, False)
# print(f.closed)


# One more important thing if we want to work with the file that is on the other directories. Then we will paste the path of file
# n = open(r"E:\Hello\file.txt")
# print(n.read())
# n.close()
# There is one more problem 
# Slashes use on the different platform 
# Windows ---> \ (backslash)
# Linux, MAC ---> / (Forward Slash)
# On the other hand pyhton is also use backslash for escape sequences
# for this problem we uses "r" for escapes
