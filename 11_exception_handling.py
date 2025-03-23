# examples of exceptions 
# dividing by 0 -- ZeroDivisionError
# priting something which is not defined -- NameError
# reading file which is not present in directory -- FileNotFoundError

# this is basically try-catch block in python 
# here is python it's try-except 

a = 5
b = 4

try: 
    c = a/b 
    # print(d)
    f = open('abc.txt', 'r')
except ZeroDivisionError: 
    print("Invalid input")
except NameError: 
    print("Variable not define")
except FileNotFoundError:
    print("Invalid file name")
except: 
    print("Something went wrong") # generic error 
finally :
    # pass
    f.close()  # finally is special block that runs with or without exceptions
# there are around 30 exceptions in python 

# Q. What will happen if finally block has exceptions
# findout 


#CREAGING OUR OWN EXCEPTIONS 
#user defined exceptions 


a = 3
if a< 18: 
    # print("You are underage")
    raise Exception("You are underage")