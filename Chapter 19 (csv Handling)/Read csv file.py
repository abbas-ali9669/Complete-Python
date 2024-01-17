# In this topic we will learn about csv (Comma Separated Value) files 
# that how we can works with csv file
# For with csv we need to import the module csv
from csv import reader

with open("file.csv", "r") as f:
    csv_reader = reader(f)    # This will give us the iterator
    # print(csv_reader)    # return iteraotr
    # now we apply the loop on it
    # if you don't want the header then you can simply skip the header line by using next() function 
    # print(next(csv_reader))
    for i in csv_reader:
        print(i)