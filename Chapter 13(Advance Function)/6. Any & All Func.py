# any() & all() function
# any() - any function only check for one value. if one value is Frue all the condtion will be True
# all() - all function check for all the value. if one vlaue is False all the condition will be False


num1 = [2,4,6,8,10]
num2 = [1,2,3,4,5,6]

# logic Method
check = []
for i in num1:
    check.append(i%2==0)
print(check)

# With all() function
check_new = all([num%2==0 for num in num1])
print(check_new)

# 2. any() function
check_new2 = any([i%2 != 0 for i in num2])
print(check_new2)



# Practice with any() all() function
# example (Value checking)
def add(*args):
    if all([(type(arg) == int or type(arg) == float) for arg in args]):
        total = 0
        for i in args:
            total += i
    else:
        return 'Wrong Input'

print(add(1,2,3,4, 'abbas'))


