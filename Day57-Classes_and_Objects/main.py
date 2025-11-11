# class Person:
#   name = "Harry"
#   occupation = "Software Developer"
#   networth = 10
#   def info(self):
#     print(f"{self.name} is a {self.occupation}")


# a = Person()
# b = Person()
# c = Person()

# a.name = "Shubham"
# a.occupation = "Accountant"

# b.name = "Nitika"
# b.occupation = "HR"

# # print(a.name, a.occupation)
# a.info()
# b.info()
# c.info()

class Animal:
    name = "Tom"
    type = "Dog"
    age= 76
    color = "Black"
    def info(self):
        print(f"This is a {self.type} and its age is {self.age}")

dog = Animal()
cat = Animal()
lion = Animal()

print(dog.name)
dog.info()