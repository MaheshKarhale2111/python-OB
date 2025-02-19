# CPP equivalent of dictionary is map or unordered map 
# it stores vaules in key - val pairs 

# created by using {}
d= {} # yeah same as set 

l = ['Mahesh', 'is','a', 'good', 'boy']

for x in l : 
    d[x] = 0
    
for x in l : 
    d[x] = d[x] + 1


# d = {'Mahesh': 1, 'is': 1, 'a': 1, 'good': 1, 'boy': 1}
    
# print(d)


# important 
# what we can use as key in dictionary -> immutable and hashale
# anthing that is immutable -> int, string, boolean ,
# we can't use list and dictionary as key element 
# tuples are immutable but hashable only if they have immutable entries 
# tuple with list entry can't be used for key 

# all other properties are same as mutable things 
# to functions, dictionary is passed as reference 
# to copy dictionary we need to use copy method. Simple assigning doesn't work 



# iterating over dictionary 
for key in d : 
    print(key, d[key])
    
    
# dictionary functions 

print(d.keys()) # (['Mahesh', 'is', 'a', 'good', 'boy'])
print(d.values()) # ([1, 1, 1, 1, 1])
print(d.items()) # [('Mahesh', 1), ('is', 1), ('a', 1), ('good', 1), ('boy', 1)])  items is a key with tuples