# In this topic we will learn the eiht block
# With block - Context Manger
with open("file1.txt") as f:    # This f is representing our variable
    data = f.read()
    print(data)



# NOTE - We dont want to close the file. Context Manger will handle this all closing system
print(f.closed)