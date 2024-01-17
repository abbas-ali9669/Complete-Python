# Dictionary Comprehension
# Example (Square)
# Simple Method 
sqr = {}
for i in range(1,6):
    sqr[i] = i**2
print(sqr)

# With Dict Comprehension
square = {i:i**2 for i in range(1, 6)}
# print(square)
for i,j in square.items():
    print(f"The number is {i} and the Square is {j}")



# Example 2 (Word Counter)
# Simple Method
string = 'Abbas'
dic = {}
for i in string:
    dic[i] = string.count(i)
print(dic)

# With List Comprehension
word = {i: string.count(i) for i in string}
print(word)