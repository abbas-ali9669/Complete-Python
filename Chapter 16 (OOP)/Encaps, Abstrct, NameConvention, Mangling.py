# in this topic we will discuss about
# 1. Encapsulation
# 2. Abstraction
# 3. Some special naming convention
# 4. Name Mangling



class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.__price = price
    # Creating instance method
    def make_call(self, phone_num):
        return f"Calling {phone_num}..."
    
    def fullname(self):
        return f"{self.brand} {self.model}"

p1 = Phone("nokia", "3310", 10000)




# Now we will discuss our topics

# 1. Encapsulation
#   write the data and the method of data written together is called          Encapsulation
# >>>> In Urdu
    # Wo data jis k sath hm functionality perform kar sakty hain wo waly methods unko aik jaga pe likhna/encapsulate krne ko he encapsulation kehty hain.
# Exmaple: See the class


# 2. Abstraction
    # Hide complexity from the user

# Example: 
    # Let's take the example of list sort method
    # Now we don't know how python sort function is working
    # Python use the ti sort algorithm for sorting the list
    # we just write the method and done our work
l = [3,4,2,1]
l.sort()    # tims sort algorihtm
# print(l)


# 4. Some special naming convention
# NOTE - There no private method/variable/class in python
# All the things are public in python language
# if we want a private variable in python then we simply add underscore (_)
# before the varible name (_variable). 
# To did this the other python developers will understand that it is private 
# varible of the class. Then they will donot change the variable value.

# some of python method name
# __name__, __dict__, __doc__ etc    these are called Dunder/magic method


# 5. Mangling
# Now the mangling is different type of concept of python. 
# =We cannot add double under score before the variable. python will not recognised the vairble. The python will the self name according to the class name 
# (__variable) = X    Python wil game the to this varibale _classanme__variable
# you can check the dictionary of the for the name that what python gives the name to your variable

# print(p1.__price)
print(p1.__dict__)    # Output >>>> {'brand': 'nokia', 'model': '3310', '_Phone__price': 10000}

print(p1._Phone__price)    # It wil works perfectly