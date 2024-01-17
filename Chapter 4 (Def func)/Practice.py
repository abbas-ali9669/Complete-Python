x = 5

def variable():
    global x
    x=10
    return x

print(x)
print(variable())
print(x)