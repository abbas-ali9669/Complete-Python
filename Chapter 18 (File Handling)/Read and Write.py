# In this topic we will wokr with 2 file we will read the data from one file and write the same the daat tothe other file

with open("file.txt", "r") as rf:
    with open("file2.txt", "w") as wf:
        wf.write(rf.read())


