# In this method we will discuss about What is Static method.
# Static method are those method that normally defines in our class
# Example
class Example:
    def __init__(self):
        pass

    # Now we are defining the static method
    # We are the predefined decorator for creating static methods
    @staticmethod
    def hello():
        x = 2
        y = 2
        return f"The Sum is {x+y}"
    
    # Example 2
    @staticmethod
    def add(x, y):
        return x+y


print(Example.add(2,3))
print(Example.hello())