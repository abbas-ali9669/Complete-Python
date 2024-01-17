# Today we will learn aout different mode of reading and writing
# "w" - Writing 
# "a" - append
# "r+" - Reading and writing

# 1. "w" - Writing
# with open("file.txt", "w") as f:
#     f.write("Hello My name is Abbas")
#     f.write("I lived in Shinkiari")
# NOTE - With the use of "w" mode there is problem with. the "w" mode will Overwrite our before stored data.
# The "w" mode wil create its own file if the file does not exist before.


# 2. "a" - Append
# with open("file.txt", "a") as f:
    # f.write("I lived in pakistan Shinkiari\n")

# NOTE - The append mode is the best mode. This will not overwrite the data 
# And write the data in the next line. This mode will also creates its own file. If the file doesn't exists


# 3. "r+" - Read and Write Mode
# with open("file.txt", "r+") as f:
#     f.seek(len(f.read()))    # This is the method of preventing overwriting
#     f.write("\nI am studying\n")
#     f.write("I am 21 year old\n")

# NOTE - The "r+" mode is the mode that we can read and write with help of "r+" mode. This method will not create its own file if the file deosn't exist.