# Class Variable
# Lets take a example of Circle
# lets find the circumference and area of circle
# Example 1
class Circle:
    pi = 3.14    #Class variable
    # The class varibale is when we define. Because the value of class variable is shared for all object
    # We donot need to define seperate object. Beacause it uses memory
    def __init__(self, radius):
        self.radius = radius
    def calc_circumference(self):
        # for calculating circumference using this formula (2*pi*radius / 2*pi*r)
        return 2*Circle.pi*self.radius

# c1 = Circle(4)
# print(c1.calc_circumference())


# Example 2 
# Suppose we have applied a discount for all items
class Laptop:
    discount = 50
    def __init__(self, Brand_name, Model_name, Price):
        self.brand = Brand_name
        self.model = Model_name
        self.price = Price
    def apply_discount(self):
        var = self.price*self.discount//100    # Use self keyword for class varible
        # Because sometimes we need to change the offer for some product
        return self.price - var

# Laptop.discount = 0    # This is when the sale is finished
    
l1 = Laptop("Dell", "INS N5050", 50000)
l2 = Laptop("Apple", "Macbook Pro", 200000)
l1.discount = 30
print(l1.apply_discount())



# NOTE - if you want to check what attribute does your object has
# print(l1.__dict__)