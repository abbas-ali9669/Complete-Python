# Exercise no.2
# In this exercise buyer input the percentage of discount that how much discount they want
# Solution 
class Laptop:
    def __init__(self, brand_name, Model_name, price):
        self.brand = brand_name
        self.model = Model_name
        self.price = price
    def discount(self, Discount_num):
        self.discount = Discount_num
        var = self.price*self.discount//100
        return self.price - var

l1 = Laptop("Dell", "InsN5050", 10000)

print(l1.discount(30))


# Method 2
class Laptop_2:
    def __init__(self, brand_name, model_name, price):
        self.brandname = brand_name
        self.modelname = model_name
        self.price = price
    def percentage(self, num):
        off_price = (num/100)*self.price
        return self.price - off_price

l1 = Laptop_2("HP", "HP 1234", 10000)
print(l1.percentage(30))