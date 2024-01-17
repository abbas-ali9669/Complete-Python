# Here we will create our first class
# we will read about/Objectives
# What is class
# How to create a class
# Whta is init method/Constructor
# What are the attributes, instance variale
# How to create our object
# Example
class Person:
    def __init__(self, fname, lname, age):    #Thee are the attributes of our class
        # Now we create the instance variable of our attributes with the help of self
        self.first_name = fname
        self.last_name = lname
        self.person_age = age
        # Now our instance variable has been created

p1 = Person('Abbas', 'Ali', 21)   # These are the objects of our class
p2 = Person('Bilal', 'Ahmad', 21)
# NOTE - When we creates the object and runs. Our init method/ constructor get called
print(p1.first_name)
print(p2.first_name)
# NOTE - If we creates two objects then the constructor get calls two time.
# It means If we have ten object the constructor get called ten time


