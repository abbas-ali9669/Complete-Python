# One Problem many solution.

# With def func()
list_ = list(range(1,11))

def o_e(l):
    new_list = []
    for i in l:
        if i%2 == 0:
            new_list.append("Even")
        else:
            new_list.append("Odd")
    return new_list

print(o_e(list_))


# With map() func
iterate = list(map(lambda a: "Even" if a%2 == 0 else "Odd", list_))
print(iterate)

# With LC (Recomended)
comp = ["Even" if (i%2 == 0) else "Odd" for i in range(1,11)]
print(comp)