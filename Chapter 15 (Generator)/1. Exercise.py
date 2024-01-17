# Define generator function
# Take one number as argument
# Generate a seqauence of even number from to number n
# Example
# if user input 10 then generate a sequence of even numbers of that particular number
def generate_num(n):
    for i in range(1, n+1):
        if i%2 == 0:
            yield i

even_nums = generate_num(10)
for i in even_nums:
    print(i)