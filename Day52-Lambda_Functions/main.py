def double(x):
  return x*2

def appl(fx, value):
  return 6 + fx(value)

double = lambda x: x * 2
cube = lambda x: x * x * x
avg = lambda x, y, z: (x + y + z) / 3

print(double(5))
print(cube(5))
print(avg(3, 5, 10))
print(appl(lambda x: x * x , 2))

import math as m

def euclidDistance(fx, x, y):
    print(f"The infinity norm of {x} and {y} is: ", fx(x, y))
    return m.sqrt(m.pow(x,2) + m.pow(y,2))

print(euclidDistance(lambda x,y: x+y, 3, 4))