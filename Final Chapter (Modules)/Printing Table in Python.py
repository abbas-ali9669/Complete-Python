# In this topic we will about how to print the table with the help of prettytable modul
from prettytable import PrettyTable

# The headers
mytable = PrettyTable(["FullName", "Age", "Standard"])

#  Add Value(rows)
mytable.add_row(["Abbas Ali", "21", "15"])
mytable.add_row(["Bilal Khan", "19", "12"])
mytable.add_row(["Mubashar Khan", "15", "10"])
mytable.add_row(["AbdulWahab", "12", "7"])
mytable.add_row(["Ali Khna", "10", "7"])
print(mytable)