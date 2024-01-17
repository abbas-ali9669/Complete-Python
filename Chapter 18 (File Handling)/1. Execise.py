# In this Exercise we have to read the data from one file and write to another file with separated form


with open("file.txt", "r") as rf:
    with open("sep form.txt", "a") as wf:
        for i in rf.readlines():
            name, salary = i.split(",")
            wf.write(f"{name}'s Salry {salary}\n")
            pass
        pass
    pass
pass
