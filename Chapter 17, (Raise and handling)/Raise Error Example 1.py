# raise error example 1
# Notimplementederror
# abstract method
class Animal:
    def __init__(self, name):
        self.name = name
    
    # NOTE - abstract method come from Java programing language and in the python we use Notimplementederror. 
    def sound(self):
        raise NotImplementedError("You have to define your own sound function")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def sound(self):
        return "bhow bhow"

class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    
    def sound(self):
        return "meow meow"


doggy = Dog("Tommy", "German")
caty = Cat("Charlie", "Persian")
print(doggy.sound())