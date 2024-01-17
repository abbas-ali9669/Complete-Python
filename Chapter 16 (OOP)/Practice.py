class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self._price = max(price, 0)
    
    @property
    def all_specs(self):
        return f"Brand '{self.brand}' Model '{self.model}' and price is '{self.price}'"
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, new_price):
        self._price = max(new_price, 0)
    
    def make_call(self, Phone_Num):
        return f"Calling {Phone_Num}..."
    

p1 = Phone("Nokia", "1100", 10000)
p1.price = -5000
print(p1.price)
print(p1.all_specs)