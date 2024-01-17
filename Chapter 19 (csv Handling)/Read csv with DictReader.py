# In this tpic we will learn about DictReader. That how we can read our csv with the help of order dictionary

from csv import DictReader

with open("file.csv", "r") as f: 
    csv_reader = DictReader(f, delimiter="|")
    for i in csv_reader:
        print(i)
# NOTE - Normally the scv file separated with cammas, But if the values are separated with any other symbols.
# for that we have function delimiter