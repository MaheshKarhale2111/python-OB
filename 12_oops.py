# class Student:
#     roll_no = None 
#     name = None 
    
# s0 = Student() # this is constructor 


# s0.roll_no = 0
# s0.name = "Mahesh"

# print(s0.roll_no, s0.name)


class Student: 
    count = 0 # count is global memeber here 
    # does not own by any particula student, there will be only one copy 
    # owned by class 
    # accessed by Student.count += 1
    def __init__(self,roll_no, name):
        # this is constructor of class 
        self.roll_no = roll_no
        self.name = name 
    
    def display(self):
        # self is container which holds current object 
        # much like this keyword 
        print(self.roll_no, self.name)
        

s0 = Student()
# s0.display()