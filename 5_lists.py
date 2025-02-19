
# list and set 
l = [1,2,"mahehsh"] # this is list 
s = {65,9,6,6} # this is set 


# l = list(range(1000000000)) 
# s = list(range(100000))


# list take less time for creating than set
# but when loopup ,list takes a lot of time than set 
print(-1 in l) # take more time
# print(-1 in s) # take less time 

# but downside of set is it's not scriptable, means we can't use s[0] 

# list.append() same as v.push_back()
# list.remove() -> removes the first occurence of element in list if present 


# more on lists 

l1 = [1,2,3] 
l2 = [4,5]

l3= l1 + l2 # we can use + operator to concenate lists 

l1 = [1,3,6]
l1 = l1*5 # [1, 3, 6, 1, 3, 6, 1, 3, 6, 1, 3, 6, 1, 3, 6], 
   

# comparison operator in lists
print([2,1] < [1,2]) # compares on one to one element basis , prints false here

# memory location lafda 
# integer example 
x = 5
y = x
x = 10
print(x,y) # will print (10,5) 

# list example 
l1 = [1,2,3]
l2 = l1
l1[0] = 100
print(l1,l2)  #[100, 2, 3] [100, 2, 3]
# this happens because lists in python are mutable and assignement operator 
# does not create new copy, it only created refrence to same object

# how to deep copy 
# method 1
l2 = list(l1)
l3 = l1[:] # slicing from start to end 
l4 =l1.copy()


# how to check if two list names poiting to same memory locatoin 
# is statement 
l5 = l1
print(l1 is l4) #false
print(l1 is l5) # true


# whenever you pass list to function
# it is passed by reference ( same as & in cpp)
# so if you pass mutable type argument then it's pass by ref
# oherwise in case of integer( immutalbe), passed by value 


# important -> Integers are immutable !!! 
# This means that once an integer object is created, its value cannot be changed in memory. Any operation that seems to "modify" 
# an integer actually creates a new integer object.


x = 10
print(id(x))

x = x + 6
print(id(x))




# another list methods 
l1 = [1,2,3]
l1.insert(2,9) # insert value at 2nd index

l1.pop(0) # remove element at 0th index 

# sorting list 

l1.sort(reverse=True)

#reverse 
l1.reverse


