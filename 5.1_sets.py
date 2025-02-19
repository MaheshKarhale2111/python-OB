# list and set comparison
l = [1,2,"mahehsh"] # this is list 
s = {65,9,6,6} # this is set 


# l = list(range(1000000000)) 
# s = list(range(100000))


# list take less time for creating than set
# but when loopup ,list takes a lot of time than set 
print(-1 in l) # take more time
# print(-1 in s) # take less time 

# but downside of set is it's not scriptable, means we can't use s[0] 


# more on sets 

s = {1,2,3,4,6,5,6}
# set is an unordered entity 
# thus it can't support indexing 
# set is mutable , but entries inside set should be immutable and hashable  
# thus you can add int to set but not list, dictionary 

# set methods 
# set derived from mathematical set so all operations in maths support here 


s2 = {1,2}
print(s2.issubset(s)) # true

#union 
c1 = s.union(s2) 
# or
c1 = s | s2 

# intersection 

c2 = s.intersection(s2)
# or
c2 = s & s2


# difference 

c3 = s.difference(s2)
# or 
c3 = s - s2
