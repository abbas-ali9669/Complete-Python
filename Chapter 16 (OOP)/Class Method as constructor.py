# now here we will create our own contructor with the help of class method
class Person:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age
    def fullname(self):
        return f"{self.fname} {self.lname}"

    # Now here we have created our class method constructor
    # Now we can create our object as we want
    @classmethod
    def own_string(cls, string):
        fname, lname, age = string.split(",")
        return cls(fname, lname, age)

l1 = Person("Abbas", "Ali", 21)    # Old Method
# print(l1.fullname())

# Own Method 
l2 = Person.own_string("Abbas,Ali,21")    # here are our own object
print(l2.fullname())