# in this topic we will learn about some more things about os module and shutil module
import os
import shutil

# 1. os.walk("path"):
# This function is for if you want the information about any foldr or directory. The walk() function will do this for. It will give you the pth, foldernames, filenames.
# path = os.walk(r'G:\Courses\Complete Python\Final Chapter')
# for current_path, folder_names, file_names in path:
#     print(F"Currrent Path {current_path}")
#     print(F"Folder Name {folder_names}")
#     print(F"File Names {file_names}")


# 2. rmdir():
# This function will remove your directory if the folder is empty otherwise the os module will not delete the folder
# os.rmdir()


# 3. makedirs():
# Thuis function will create folder inside folder
# os.makedirs("new/new2")

os.chdir(r'F:\Home')

# Now finally the shutil mdoule


# 1. shutil.rmtree():
# this functon will remove the foldr even the folder is empty or not. And remember this function will not send yur file or folder to recyclebin 
# shutil.rmtree("new2")


# 2. shutil.copytree():
# This function will copy the folder from one plce to another
# shutil.copytree("h1", "h2/h1")    #inthe last we can rename this file 


# 3. shutil.copy():
# This function is for copy the file form one place to another.
# shutil.copy('fiel.txt', "h2/file.txt")
# Same we can rename the file in last 


# 4. shutil.move():
# This function will move oyr file or folder from one place to another
# shutil.move("fiel.txt", "h1/file.txt")    # With file

# shutil.move("h1", "h2/hy1")

# The End:)
