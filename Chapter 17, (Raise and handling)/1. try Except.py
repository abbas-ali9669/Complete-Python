# In this topic we will now discuss about try except
# Exception Handling
# Four Keywords of EXCEPTION HANDLING
# try, except, else, finally.
# Q - What is exception
# A - Error that occurs while execution



# age = int(input("Enter Your age : "))    # In this section we want the 
# integer input form the user. what if user input the string. the value 
# error occurs. for the handling of value error we use try except block
# If we input the wrong type the vlaue error occur

# Now we want the infinite loop that run until the user didnot enter the correct value
while True:
    try:
        age = int(input("Enter Your age : "))
        break
        # If user input the correct value the age variable will create otheriwse the variable will not create
    except ValueError:
        print("You entered the wrong input. Integer required")
    except:
        print("Unexpectedly Error...")




if age < 18:
    print("You can't play this game")
else:
    print("You can play this game")
