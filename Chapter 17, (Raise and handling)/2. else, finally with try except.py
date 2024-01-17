# in this topis we will discuss about else, finally blocks
while True:
    try:
        num = int(input("Enter a number : "))
        # NOTE - We can add more line intthe try block
        # But this is not the the good way to add line in try block 
        # This will decrease the readability of code. we can add extra lines 
        # into the else block instead of writing in the try block
    except ValueError:
        print("You've entered the wrong input pleasem try int")
        print("num b/w 0,9")
    except:
        print("Unexpected Error")
    # Here are the else block. 
    # Q - When else block runs
    # A - when the try block runs succesfully the else block will run ass well
    # along with the try block. we should write the extra code of try block in this block
    else:
        print(f"User input = {num}")
        break
    # In the last the the finally block. 
    # Q - When finally block is executes ?
    # A - finally block executes in every situation even try, except, else, 
    # runs or not 
    finally:
        print("This is finally block")

if num > 18:
    print("You Can Play")
else:
    print("You Cannot Play")
    print("Your age must have 18+")
