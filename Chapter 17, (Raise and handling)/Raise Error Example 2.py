# Raise Error Example 2
class Mobile:
    def __init__(self, name):
        self.name = name

class Mobilestore:
    def __init__(self):
        self.mobile = []
    
    def add_mobile(self, new_mobile):
        if isinstance(new_mobile, Mobile):
            self.mobile.append(new_mobile)
        else:
            raise TypeError("New mobile should be the object of Mobile class")

one_plus = Mobile("One Plus 6")
samsung = "Samsung Galaxy S8"    # String. And we don't want to add the string
mobostore = Mobilestore()
# print(mobostore.mobile)
# mobostore.add_mobile(samsung)    # Now this string will not add Because this is not the part of mobile class
mobostore.add_mobile(one_plus)    # Now this is the object of mobile class
mobo_phone = mobostore.mobile
print(mobo_phone[0].name)