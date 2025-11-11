class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def make_sound(self):
        print("Sound made by the animal")

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed
        
    def make_sound(self):
        print("Bark!")

d = Dog("Dog", "Doggerman")
d.make_sound()

a = Animal("Dog", "Dog")
a.make_sound()

# Quick Quiz: Implement a Cat class by using the animal class. Add some methods specific to cat

class Cat(Animal):
    def __init__(self, name, age, color):
        Animal.__init__(self, name, species= "Cat")
        self.age = age
        self.color = color
    
    def make_sound(self):
        print("Meowwwww")
c = Cat("Brixton", 7, "Orange")
c.make_sound()
print(c.species)