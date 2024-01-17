# This is Challenge

# define a function take any no of lists containing number 
# [1,2,3], [4,5,6], [7,8,9]
# return average
# (1+4+7)/3, (2,5,8)/3, (3,6,9)/3

# with 2 list 
def average_finder(l1,l2):
    average = []
    for i in zip(l1,l2):
        average.append(sum(i)/len(i))
    return average

# print(average_finder([1,2,3], [4,5,6]))

# with Unlimited list
def average_finder2(*args):
    everage = []
    for i in zip(*args):
        everage.append(sum(i)/len(i))
    return everage

print(average_finder2([1,2,3], [4,5,6], [7,8,9]))

# with lambda
average3 = lambda *args: [sum(i)/len(i) for i in zip(*args)]
print(average3([1,2,3], [4,5,6], [7,8,9]))