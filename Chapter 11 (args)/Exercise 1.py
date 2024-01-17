# define a function
# input

# num, iterable(tuple, list) containing number as args 

# example
# nums = [1,2,3]
# to_power(3, *nums)

# Output
# list ---> [3, 8, 27]

# if user didn't pass any args give user a message "Hey you didn't pass any args"

# else
# return list

# NOTE - USE list comprehension


# Solution
# With List Comprehension
def to_power(num, *args):
    if args:
        return [i**num for i in args]
    else:
        return "You didn't pass anything"


print(to_power(2,*[2,3]))


# Without List Comprehension
def to_power_2(num, *args):
    list_ = []
    for i in args:
        if args:
            list_.append(i**num)
        else:
            print("Youdidn't Pass Anything")
    return list_


print(to_power_2(2, *[2,3]))



# With Dictionary (with Comprehension)
def too_power_3(num, *args):
    if args:
        return {i:i**num for i in args}
    else:
        return "You Didn't Pass Anything"

print(too_power_3(2, *[2,3,4]))


# Without Dict (Comprehension)
def too_power_4(num, *args):
    dic = {}
    for i in args:
        if args:
            dic[i] = i**num
        else:
            "You Didn't Pass Anything"
    return dic

print(too_power_4(2,*[2,3,4]))