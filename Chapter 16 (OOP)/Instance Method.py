# Instance Method
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    # Now here we will define instance method
    # Those func that define in class called method/function
    # For printing fullname 
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
        pass
    # Now defning a method for checking age>18
    def check_age(self):
        return self.age>18

# Objects
p1 = Person('Abbas', 'Ali', 21)
p2 = Person('Ahmad', 'jamil', 15)

# 1.
# Now checking for fullname
# There are two methods for printing
# method 1
print(p1.full_name())    # Most commonly used
# method 2
print(Person.full_name(p1))    # Rarely used
# Both are same method 

# 2.
# Now check for object age
# Method 1
print(p1.check_age())    # Most commonly used
# Method 2
print(Person.check_age(p1))    # Most Rarely used

# Structures for both
# 1. classname.function(object)
# 2. object.function()
print(Person.check_age(p2))

# defining 2 method
# method = classname.function(object)
# Actually this syntax is for python that how python is working in bacnkend
# for example (List)
l = [1,2,3]
# for deleting item
# l.pop(0)    # This method is delete the last item of or list
# How This runs in background
list.pop(l, 0)    # In the backend of python this hepppens
# for adding item
# l.append(4)    #default method
list.append(l, 4)    # this happens in the backend of python 

