# In this section we will cover class method
# We will create a class method taht calculate the object of our class
class Person:
    count_obj = 0
    def __init__(self, fname, lname, age):
        Person.count_obj += 1
        self.fname = fname
        self.lname = lname
        self.age = age

    def full_name(self):
        return f"{self.fname} {self.lname}"
    
    def check_age(self):
        return self.age > 18
    
    # Class method (a predefined decorator)
    @classmethod
    def count_instance(cls):
        return f"You have created {cls.count_obj} instances of {cls.__name__} class"
    
    
# Object 1
p1 = Person("Abbas", "Ali", 21)


# Object 2
p2 = Person("Ali", "Khan", 21)


# Check Instances
print(Person.count_instance())


