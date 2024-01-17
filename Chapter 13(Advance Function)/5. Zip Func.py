# Zip() Function
# Use for combine lists
# Example


user = ['user1', 'user2', 'user3']
name = ['Abbas', 'Ahmad', 'Ali']
# last_name = ['Ali', 'Jamil', 'Sher']

zip_ = tuple(zip(user, name))

# print(zip_)

# Loop
# n = 1
# for i, j in zip_:
    # print(f"{i} and name of {i} is {j}")
    # n += 1



# Practice with zip() function
l1 = [1,3,5,7]
l2 = [2,4,6,8]

# Unpack this
l = [(1, 2), (3, 4), (5, 6), (7, 8)]
# Unpack_ = list(zip(*l))
l3, l4 = zip(*l)
print(list(l3))
print(list(l4))

# Fnd the maximum of l1 and l2
new = []
for pair in zip(l1, l2):
    new.append(max(pair))
print(new)


# My methods of unpacking
l1 = []
l2 = []
for i, j in l:
    l1.append(i)
    l2.append(j)
print(l1)
print(l2)