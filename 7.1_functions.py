# Functional programming part 2 
# ------------------------------------------------------------ 

# in line statements 
a = 5 
b = 10 

small = a if a < b else b # saves 4 lines of code 


# one line statement for loop 
l = [5,68,3,2,4,8]
''' 

c = []
for x in l: 
    if x %2 == 0: 
        c.append(x)
'''

c = [x for x in l if x % 2 == 0]


# other examples of list comprehention 

numbers = [x for x in range(10)] # creates a list [0,1..... 9]




# ---------------------------------------------------------------------------------------- 
# functional programming part 3 

# Lambda funtions
# A lambda function in Python is a small, anonymous function that can have any number of arguments 
# but only one expression. It is defined using the lambda keyword.

def add1(x,y):
 return x+y 

add2 = lambda x,y : x + y # so function is stored in a variable called add2 
print(type(add2)) # type is class function
# but calling of function is similar 

print(add2(5,6))


# Enumerate
# What is enumerate() in Python?
# enumerate() is a built-in function in Python that adds an index (counter) to an iterable (list, tuple, string, etc.), 
# returning it as an enumerate object. This is useful when you need both the index and the value while iterating.

fruits =["Apple", "Banana", "Orange", "kiwi"]

for i in enumerate(fruits):
    print(i)
# equivalent to for i in range(len(fruits)) print(i,fruits[i])


# zip function 
# Couple two or more iteretable entities into tuples , saves lines of code 

lenth = [5,6,6,4]

print(list(zip(fruits,lenth))) # [('Apple', 5), ('Banana', 6), ('Orange', 6), ('kiwi', 4)]
# zip Stops when the shortest iterable is exhausted.




# Map function 
# The map() function applies a given function to all elements in an iterable
# (like a list, tuple, etc.) and returns a map object (which is an iterator).

def square(x): 
    return x*x 

a = [1,2,3,4]
c = map(square,a)
# print(list(c)) # [1, 4, 9, 16]

def addlist(x,y): 
    return x+y
b = [2,6,7,5]
c = map(addlist,a,b)
# add two list in single line 
print(list(c))




# filter function 

def isEven(x):
    return x % 2 == 0   # it should return a boolean 


c= filter(isEven,a)
print(list(c)) # [2,4] 