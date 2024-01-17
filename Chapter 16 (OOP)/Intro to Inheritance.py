# Today we will discuss about inheriatnce
# Inheriatance is all about to use the function of parent/base class
# we don't need to rewrite the code again and again
# Use of DRY Principle
class Phone:    # Base/ Parent class
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    
    def full_name(self):
        return f"{self.brand} {self.model}"

# Now we will use inheritance
class Smartphone(Phone):    # Derived/Child Class
    def __init__(self,brand, model, price, ram, rom, rear_camera):
        # now here we will use inheritance for first attributes
        # There are two method of inheritance
        # Phone.__init__(self, brand, model, price)    # Uncommon way
        super().__init__(brand, model, price)
        self.ram = ram
        self.rom = rom
        self.rear_camera = rear_camera


p1 = Smartphone("Nokia", "3310", 10_000, "512mb", '1gb', "1mp")
print(p1.rear_camera)

# NOTE - We will cover more lacture later 
# (Multilevel Inheritance, MRO, Method Overriding, Multiple Inheritance, Special magic/dunder methods, Polymorphism)

