# In this topic we will discuss property and setter decorator
# 1. Property
# 2. Property Decorator getter(), setter()
class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        # There is one problem. what if we add negative price 
        # For not adding negative we have two methods
        # 1. if, else
        # 2. max() func
        # self._price = max(price, 0)
        if price > 0:
            self._price = price
        else:
            self._price = 0
        
        # There is one problem with instance vairable 
        # if we change the price of object next to object this will no be update. The god method is to define function (instance method)
        # self.comp_specs = f"{self.brand} {self.model} and price is {self._price}"
    
    def comp_specs(self):
        return f"{self.brand} {self.model} and price is {self._price}"


p1 = Phone("Nokia", "1100", -10_000)    # The price will be show 0 if we put negative price
# p1._price = -500
# print(p1._price)
# print(p1.comp_specs())    # If we want to treat this as a instance vairable means print it without variable. So we the porperty getter and setter.


# 2. Property Decorator
# NOTE - in the place of using getter() method we use @property decorator
# and in the place of using setter() we define as a @getter func name 
class Phone_2:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self._price = max(price, 0)
    
    # If we want to treat this as instance variable like no paranthesis while calling this function. Then we have to set a decorator @property
    @property
    def full_specs(self):
        return f"{self.brand} {self.model} and the price is {self._price}"

    @property    # >>>> This is the getter()
    def price(self):
        return self._price
    
    @price.setter
    def price(self, new_price):
        self._price = max(new_price, 0)



p2 = Phone_2("Samsung", "S10", 15000)
p2.price = -500
# print(p1._price)
print(p2.price)
print(p2.full_specs)