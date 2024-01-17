# Dictionary Comprehension with if else
# Example {1: 'odd', 2: 'even'}
# With List Comprehension
d = {i:('Even' if i%2 == 0 else 'odd') for i in range(1,11)}
print(d)

# With Simple Method 
dic = {}
for i in range(1, 11):
    if i%2 == 0:
        dic[i] = 'Even'
    else:
        dic[i] = 'Odd'
print(dic)