from csv import writer


with open("Write_file.csv", "w", newline="", encoding="UTF-8") as f:
    print(f.encoding)
    csv_writer = writer(f)
    # NOTE - There are two method to write the file
    # 1. writerow([])
    # 2. writerows([],[],[])

    # 1. writerow
    # csv_writer.writerow(["Name", "Country"])
    # csv_writer.writerow(["Abbas", "Pakistan"])
    # csv_writer.writerow(["Bilal", "Pakistan"])

    # 2. writerows
    # We can make multiple rows in one line wih the help of writerows
    csv_writer.writerows([["name", "country"], ["Abbas", "Pakistan"], ["Bilal", "Pakistan"]])