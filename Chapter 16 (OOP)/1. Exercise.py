# Create a laptop class with attributes like (brand_name, Model_name, Price)
# Create two object/ isinstance of your laptop class

# Solution
class laptop:
    def __init__(self, brand_name, model_name, price):
        #These are instance variables
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price
        self.all_info = brand_name + " " + model_name
        # We can create this type of instance varianble for showing all info of our attributes

l1 = laptop("Dell", "Inspiron N5050", 50000)
l2 = laptop("Hewllet Packard", "HP 1234", 55000)
print(l1.brand_name, l1.model_name, l1.price)
print(l2.brand_name)

print(l1.all_info)