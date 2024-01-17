import random 
lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num = '0123456789'
symb = '[]{}()/,._'
all = lower + upper + num + symb
lenght = 8
password = "".join(random.sample(all, lenght))
# print(password)