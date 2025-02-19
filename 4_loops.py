# for i in range(1,11,2) :  # third parameter is step , same as in c++ 
#     print(i)              # 1 is starting point, 11 is limiting, and 2 is i = i+2


# for i in range(10,-1,-1) : # step size is required in printing backwards 
#     print(i)


# for i in range(0,10) :
#     print(i,end=" ")

d = 2
m = 8
y = 1969

# print("Today's date is", end=" ")
# print(d,m,y,sep = "-")

#curly braces kind of functionality in python 

print(f'day is {d} month is {m} year is {y}')
#another way 
print(' day is{0},month is {1}, year is{2}'.format(d,m,y))


# for printing decimal values 
pi = 22/7
print(f'value of pi is {pi :.2f}')


# for right aligning 
print('{0:5d}'.format(1))