# In this topic we will learn about Read and Write simultaneously.
# there are many combination that you can use reader & dictreader
# Writer & dictwriter its up to you that waht combinaton you want to use.
from csv import DictReader, DictWriter


with open("dictwriter.csv", "r") as rf:
    with open("Read Write Simultaneously.csv", "w", newline="") as wf:
        csv_reader = DictReader(rf)
        csv_writer = DictWriter(wf, fieldnames=["FullNames", "Phones"])
        csv_writer.writeheader()

        for i in csv_reader:
            fname, lname, phone = i["FirstName"], i["LastName"], i["phone"]
            # Now here we will extract fullnames and phone
            csv_writer.writerow({
                'FullNames':fname+lname,
                "Phones":phone
            })