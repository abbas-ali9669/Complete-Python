# In this topic we will learn about writing in csv using dictwriter
from csv import DictWriter

with open("dictwriter.csv", "w", newline="") as f:
    csv_writer = DictWriter(f, fieldnames=["FirstName", "LastName", "Age"])
    csv_writer.writeheader()
    # Now this will give us an iterator 
    # Now here is two method of writing in csv with dictwriter
    # 1. writerow({})
    # 2. writerows([{}, {}, {}])

    # 1. Writerow
    # csv_writer.writerow({
    #     "FirstName":"Abbas",
    #     "LastName":"Ali",
    #     "Age":21
    # })

    # csv_writer.writerow({
    #     "FirstName":"Bilal",
    #     "LastName":"Ahmad",
    #     "Age":19
    # })

    # 2. Writerows
    csv_writer.writerows([
        {"FirstName":"Abbas",
        "LastName":"Ali",
        "Age":21},

        {"FirstName":"Bilal",
        "LastName":"Ahmad",
        "Age":19},

        {"FirstName":"Ahmad",
        "LastName":"Khan",
        "Age":25}
    ])