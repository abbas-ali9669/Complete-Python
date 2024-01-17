# Set Comprehension ---> Only One Lecture (Simple Like List)

# Example (Square)
s = {i**2 for i in range(1,11)}
print(s)

# Example 2 (Name First Letter)
names = {'Abbas', 'Bilal', 'Mubashar'}
s2 = {i[0] for i in names}
print(s2)


# For Practice 
names1 = {'Abbas', 'Bilal', 'Mubashar'}
s3 = {('Present' if 'Abbas' in names1 else 'Not Present')} 
print(s3)