#single heritance
class A:
    def displayA(self):
        print("inheritance A Class")
class B(A):
    def displayA(self):
        print("inheritance B Class")
obj=B()
obj.dispalyA()
obj.displayB()
# multilevel inheritance
class A:
    def displayA(self):
        print("inheritance A Class")

class B(A):
    def dispalyB(self):
        print("inheritance B Class")

class C(B):
    def displayC(self):
        print("inheritance C class")
obj=c()
obj.displayA()
obj.displayB()
obj.dispalyC()
    


