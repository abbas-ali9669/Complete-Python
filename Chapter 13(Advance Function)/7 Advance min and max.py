# Advance min() and max() function
# example (Previous Method)
num = [1,2,3,4,5,6,7]
# print(min(num))

# example (New method find with lenght of string)
# NOTE - You can use it min and max as you want
def func(item2):
    return len(item2)

name = ['abbas', 'bilal', 'Mubashar', 'Ali']
print(max(name, key=len))    #----> Find according to lenght
print(max(name, key= lambda item: len(item)))    #----> with lambda function
print(max(name, key=func))    #----> with def function


# Example (with List)
student1 = [
    {'name': 'Abbas', 'age': 21, 'score': 90},
    {'name': 'Ahmad', 'age': 25, 'score': 75},
    {'name': 'Ali', 'age': 23, 'score': 66},
]
print(max(student1, key=lambda k: k.get('score')).get('name'))
# My Method
print(max(student1, key=lambda k: k['score'])['name'])




# With nested dict
student2 = {
    'Abbas': {'age': 21, 'score': 45},
    'Ahmad': {'age': 25, 'score': 39},
    'Ali': {'age': 23, 'score': 34}
}
print(max(student2, key= lambda a: student2[a].get('score')))



# With User Defined func
# Student 1
def func1(item):
    return item['score']

# Student 2
def func_2(item_2):
    return student2[item_2]['score']