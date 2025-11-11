# class Employee:
#   def __init__(self, name):
#     self.name = name
#   def show(self):
#     print(f"The name is {self.name}")

# class Dancer:
#   def __init__(self, dance):
#     self.dance = dance

#   def show(self):
#     print(f"The dance is {self.dance}")

# class DancerEmployee(Employee, Dancer):
#   def __init__(self, dance, name):
#     self.dance = dance
#     self.name = name

# o  = DancerEmployee("Kathak", "Shivani")
# print(o.name)
# print(o.dance)
# o.show() 
# print(DancerEmployee.mro())

class Parent1:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # def parNum(self):
    #     print("The parent number is 1")

class Parent2:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def parNum(self):
        print("The parent number is 2")

class Parent3:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def parNum(self):
        print("The parent number is 3")

class Child(Parent1, Parent2, Parent3):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def parNum(self):
        print("The parent number is 0")

child = Child("Ajay", 25)
print(Child.mro())
child.parNum()