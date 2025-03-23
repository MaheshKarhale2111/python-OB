class Person:
    def __init__(self, name, age):
        self.name = name 
        self.__age = age # making it private
    
    def display(self): 
        print(self.name, self.age)
        
class Student(Person): # way of inheriting 
    def __init__(self, name, age, marks):
        super().__init__(name,age) # execute init method from parent
        self.marks = marks 
    
    def display(self): 
        super().display()
        print(self.marks)
        
class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name,age)
        self.salary = salary
    
    def display(self): 
        print(self.name, self.age, self.salary)
        # display method was present originally 
        # here we overriding it 



s = Student("Mahesh", 20, 100)
s.display()

e = Employee("Mahesh", 20, 25000)
e.display()

        