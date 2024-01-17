import time
# list vs Gnerator
# We wil check the memory usage and  time
# when to use list, and when to use generator

# 2. 
t1 = time.time()
list_ = [i**2 for i in range(10000000)]
# List uses 400mb memory to generate the square of 10 million numbers
# for checking memory usage - Start the task manager and see the memory usage
print(time.time() - t1)
# list took approximately 5 second (4.5739991664886475)


t2 = time.time()
gen = (i**2 for i in range(100000000))
# Generator used tje 0.0mb memory for generate the square of 100 million numbers
print(time.time() - t2)
# genertor took 0.0 second


# 3. 
# Q - When to use list
# A - list is when you have to work with yor sequaence many time. And you want to store your sequaence 

# Q - When to use generator
# A - generator is when you have to work with your sequence with only present time or one time then the generator is very best
