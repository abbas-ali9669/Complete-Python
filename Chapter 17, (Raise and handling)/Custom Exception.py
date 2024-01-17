# In the custom exception we make our own Erro for the better readabilty
# With creating our own errors we ca give the clear message to the user


class NameTooShotError(ValueError):
    pass
# Here we will inherit the class of value Error

def validate(name):
    if len(name) < 8:
        # Now here we will create our pwn error
        raise NameTooShotError("Name is too short")
    return f"Hello {name} !!!"

name = input("Enter Your Name : ")
check = validate(name)
print(check)