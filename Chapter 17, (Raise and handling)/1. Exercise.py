# In this exercise we will hane the division Error
try:
    num_1 = int(input("Enter two number : "))
    num_2 = int(input("Enter two number : "))
    result = num_1/num_2

except TypeError:
    print("Please enter both integer numbers")
except ValueError:
    print("Please input the right num b/w 0,9")
except ZeroDivisionError:
    print("The Numbers cannot divide by zero")
except:
    print("Unexpected Error")
else:
    print(result)



# Solution 2
def divide(a, b):
    try:
        return a/b
    except ZeroDivisionError as err:    # Here we can print teh lines of original Errors by using the as keyword
        return f"{err}: The number cannot divide by zero"
        # return err
    except TypeError as err:
        return f"{err}\nDataTypeError: Int require."
    except:
        return f"Unexpected Error"

print(divide(10,0))



