from csv import DictReader, DictWriter

with open("dictwriter.csv", "r") as rf:
    with open("file.csv", "w", newline="") as wf:
        csv_reader = DictReader(rf)
        csv_writer = DictWriter(wf, fieldnames=['Name',"Phone"])
        csv_writer.writeheader()

        for i in csv_reader:
            name, phone = i["FirstName"], i["phone"]
            csv_writer.writerow({
                "Name":name.upper(),
                "Phone":phone
            })