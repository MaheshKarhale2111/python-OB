# in operator in python 
print("mahesh" in "mahesh pralhad karhale")# return boolean 


#chaining comparison operators in python works 
x = 5
print(1 < x < 10)

#spacing in print statement 
print("mahesh \t karhale") # gives one tab space 
print("mahesh\nkarhale")  # prints in new line

s = "mahEsh"
print(s.lower()) #mahesh
print(s.upper()) #MAHESH
print(s.title()) #Mahesh\



# isdigit() -> checks if all entries in string are digits 
# isalpha -> check if all entries in string are alphabets
# isalnum() -> checks digit and alphabets

#for trimming, python has strip 
a = "   hello  "
print(a.strip()) # removes white spaces 
print("-@@-hello---@".strip('-@')) # output hello, #removes the characters mentioned in the strip function 
# there is also rstrip() and lstrip() to only remove characters from left and right side 
print("---hel--lo----".strip('-')) # strip does not remove characters inbetween 

# startswith('P')
# endswith('n')


print("hello".count('l')) # gives count of character l
print("hello".index('o')) # gives index of 'o'
print("hello".replace('ll','L')) # returns "heLo"
#IMP : IN python strings are immutable,means once declared they can't be chagned
# means s[3] = 't' is not allowed ( bit shock from c++)

#if you want to do that 
text = 'abcdefg'
text = text[:1] + 'Z' + text[2:]


s = "hello"
p = s
# p and s are pointing to same object location in python 
# to copy new string 
p = s[:]

# print the line #->Double forward slash // and Double backward slash \\
print("Double forward slash // and Double backward slash \\\\") 
# we need escape character for quotes and '\'(backward slash as they have meaning in python )
# but for forward slash we don't need any escape sequence 

print("mahesh \a karhale")

