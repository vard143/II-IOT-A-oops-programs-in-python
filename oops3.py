class Employee:
    def __init__(self,name,age):
        self._name=name
        self._age=age
class SubEmployee(Employee):
    def show_age(self):
        print("age:",self_age,"name:",self._name)

emp=SubEmployee("boss ra",20)
print(emp.name)
emp.show_age()
