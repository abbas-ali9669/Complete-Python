# In this exercise we wull count the instance/object of class 
# that how much instance in this class
# Solution
class Teacher:
    instance = 0
    def __init__(self, name, ID, age, address):
        self.name = name
        self.id = ID
        self.age = age
        self.address = address
        # self.all_data = f"{self.name} {self.id} {self.age}"
        Teacher.instance += 1

obj = Teacher("Abbas Ali", 1, 21, "Shinkiari")
obj2 = Teacher("Ali Khan", 2, 19, "Mansehra")
obj3 = Teacher("Ahmad Khan", 3, 25, "atd")
print(Teacher.instance)
# Now Here we will count the object and knows how many object does our class has