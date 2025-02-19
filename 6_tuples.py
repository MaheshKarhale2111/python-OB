# list is create with []
# set is created with {}
# tuple is created with ()

# tuple looks like list, you can access elements via index 
# but you can't append or remove element from it 
# TUPLE IS IMMUTABLE 

# WHEN YOU don't wanna change something you use tuple 
# but why ? 

# tuple takes less space 

# say you have list l and tuple t 
l = list(range(10))
t = tuple(range(10)); 

print(l.__sizeof__()) 
print(t.__sizeof__())

# how does tuple take less memory? it stores in slightly different way 


# more on tuples 
# packing and unpacking using tuple 

t = 1,2,3 # we didn't specifically state to make tuple but computer converted it to tuple 
print(t,type(t)) # this is called packing 3 values int single entity 

x,y,z = t
print(x,y,z) # unpacking


# swapping 

x,y = y,x # here, inside, python is packing x,y into tuple and then unpacking 

# creating tuple with single value 

t = (10)
print(type(t)) # prints integer

t = (10,) # added extra comma 
print(type(t)) # prints tuple


t = ([1,2],['a','b'])

t[0][0] = 200
print(t) #([200, 2], ['a', 'b'])
# if there is list inside list, we can modify values inside list 
# this principle is called as hashable 

# if values inside tuple are immutable then tuple considers as hashable 
# if values inside tuple are mutable then tuple is non-hashable 

t1 = (1,2,3) # hashable 
t2 = ([1,2,3],) # non-hashable
