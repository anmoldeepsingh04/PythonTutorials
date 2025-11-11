# class Person:

#   def __init__(self, name, occ):
#     print("Hey I am a person")
#     self.name = name
#     self.occ = occ

#   def info(self):
#     print(f"{self.name} is a {self.occ}")


# a = Person("Harry", "Developer")
# b = Person("Divya", "HR") 
# a.info()
# b.info()
# # print(a.name)
# # a.name = "Divya"
# # a.occ = "HR"
# # a.info()

class Animal:

    def __init__(self, name, type, age, color):
        print("This is being called!")
        self.name = name
        self.type = type
        self.age = age
        self.color = color
    
    def info(self):
        print(f"This is a {self.type}, whose name is {self.name}. {self.name}'s age is {self.age} and its color is {self.color}.")

dog = Animal("Tom", "Dog", 8, "Golden")
dog.info()