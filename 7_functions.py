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
