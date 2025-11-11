class MyClass:
  def __init__(self, value):
      self._value = value
    
  def show(self):
    print(f"Value is {self._value}")
    
  @property
  def ten_value(self):
      return 10* self._value
    
  @ten_value.setter
  def ten_value(self, new_value):
      self._value = new_value/10

obj = MyClass(10)
obj.ten_value = 67
print(obj.ten_value)
obj.show()

# class Animal:
#     def __init__(self, type, age):
#         self._type = type
#         self._age = age
    
#     def show(self):
#         print(f"The age is {self._age}.")
    
#     @property
#     def vals(self):
#         return 10 * self._age
    
#     @vals.setter
#     def vals(self, newAge):
#         self._age = newAge
    
# dog = Animal("dog", 9)
# print(dog.type, dog.age)
