# type of function argument 
# 1. positional arguments 
#     Where sequence of argument is critical wrt to execuation of function defination
# 2. Keyword arguments
# 3. default argument 



def add(c,a,b):
    return (a+b-c)
    
print(add(a = 20,b = 30,c= 40)) # keyword argument 

def add2(c,a = 20, b = 30): # default arguments 
    return (a+b-c)

print(add2(40))

# types of functions 
# print is function 

# 1. Inbuilt functions
    # eg. print(), input(), len()
# 2. Library functions
    # eg. log(), calendar(), random()
# 3. Methods 
    # upper(), lower()
# 4. User defined functions 
    # def add(a,b)


# scope of variables 
# in python int,float,bool, tuple are passed by value 
# and dictionary, list, set are passed by ref


def fun1():
    global x # this way function doesn't create a new varialbe scope to itself, it searches for global 
    # variable name x and do operation on it
    x = x*2
    print("The new variable is ", x)

x = 5

# print("value of x is ", x)
# fun1()
# print("value of x is ",x )





# functional programming in python part 1 
# How iter() Works
# It returns an iterator object that allows iteration over the given iterable one element at a time.
# You can then use next() to get the next item.


fruits = ["Mango", "Apple", "Orange", "Banana"] 

basket = iter(fruits)
print(basket) #list iterator 

print(next(basket)) # mango
print(next(basket)) # apple
print(next(basket)) # orange

# why we need iter ? 
# iterate over iterable entity , give functionality of lazy 
#nstead of storing all elements in memory at once, an iterator fetches elements one at a time 



# generators 
# A normal function runs once and returns a value using return.
# A generator function uses yield instead of return, allowing it to pause and resume execution.

# Example: Generator That Yields Numbers


def my_generator():
    print("Starting...")
    yield 1
    print("Paused...")
    yield 2
    print("Paused again...")
    yield 3
    print("Finished.")

gen = my_generator()  # Creates the generator but does NOT run it yet

print(next(gen))  # Output: "Starting..." then 1
print(next(gen))  # Output: "Paused..." then 2
# print(next(gen))  # Output: "Paused again..." then 3


# Key Differences From Normal Functions:

# Does not execute immediately; it returns a generator object.
# Pauses at yield and resumes from the last yield point when next() is called.
# Stops with StopIteration when there are no more yield statements.


# Instead of storing all items in memory, generators produce values one at a time, making them efficient.

# Normal list (stores all values in memory)
nums_list = [x**2 for x in range(1000000)]  

# Generator (does not store all values)
nums_gen = (x**2 for x in range(1000000))  

import sys
print(sys.getsizeof(nums_list))  # Large memory usage
print(sys.getsizeof(nums_gen))   # Much smaller memory usage





