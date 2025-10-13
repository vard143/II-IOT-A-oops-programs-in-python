# example 2 school management
#parent
class person:
    def __init__(self,name,age):
        self.Name=name
        self.Age=age
class Student(person):
    def __init__(self,name,age,rollno=345):
        super()__init__(name,age)
        self.rollno=rollno

def introduce(self):
    print("my name is {self.Name},rollno:{self.rollno}")

obj=Student("vardhan",le3)
obj.introduce()
    
