print(type(1+4/2))
# it is float , 
# the reason being the division operator returns in float. 
# so it is 1 + 2.0 = 3.0 which is float 


print(type('c'))
# It is str. There is no char in python 
#
# 


# reversing string n python
# not as straightforward as c++ 
a = "mahesh"
reversed_a = a[::-1]
print(reversed_a)
print(a[::2]) # get every second character of string , interesting


output4 = '-'*50 # str: just the hypen "-" repeated 50 times


# ***
# Rule on variable name 
# it has to be alphanumeric with only one special character allowed - (_) underscore 
# Name can't start with a number

_ = 6 # this is allowed ( can make good interview question)

# deleting a variable
a = 6
del a # this will delete variable a


# in operator in python 
print("mahesh" in "mahesh pralhad karhale")# return boolean 


#chaining comparison operators in python works 
x = 5
print(1 < x < 10)

#spacing in print statement 
print("mahesh \t karhale") # gives one tab space 
print("mahesh\nkarhale")  # prints in new line

# rouding in python 

x = 5.5666 
print(round(x,2))