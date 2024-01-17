# Today we are going to discuss os module (Operating System module)
# this is very important and easy module
import os
# 1. Getting current working directory
print(os.getcwd())

# # 2. For creating Folder
# os.mkdir("Practice")    # Once the folder create we cannot make the other folder with the same name

# 3. Check the folder/file already exists ?
# print(os.path.exists("Practice"))
# method 2 with if else
# if os.path.exists("Practice"):
#     print("Already Exists")
# else:
#     os.mkdir("Practice")

# 4. For file Creation
# There are many ways to create a File
# open("file.txt", "a").close     # Benefit of using this method. If file is already exists this mwthod will not give you an error. And donot create a file

# 5. For chnging the directory
# There are 2 method 

# 1. Make a folder and give the full path
# os.mkdir(r"F:\Hello")

# 2. use the os func
# os.chdir('F:\Hello')


# 6. For printing list of your path information. That waht file and folder exist in oyur path
# print(os.listdir())
# If you want to know any other drive information list. As usual there is two method 
# 1. Change your current working directory
# 2. Put the path address where do you need the info 
# print(os.listdir('F:\AUDIO'))


# 7. Printing Path of every file and folder
# There are tow ways 
# 1. This is not the good way of getting path of 
# for i in os.listdir():
#     print(r"G:\Courses\Complete Python\Final Chapter" +"\\"+ i)     # Not Recomended. Because in the MAC and linux OS using forward slashes (/)

# 2. Recomended way
for i in os.listdir():
    print(os.path.join("G:\Courses\Complete Python\Final Chapter", i))
    # print(os.path.join(os.getcwd(), i))
    # Both lines we can use

# 8. For Directory deletion. But if the folder is not empty the os module cannot delete the folder/directories
os.rmdir("")    # Put your path or name

# 9. For file Deletion 
os.remove("")    # Put your path or name


