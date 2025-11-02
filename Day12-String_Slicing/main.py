fruit = "Mango"
mangoLen = len(fruit)
print(mangoLen)
print("1 ", fruit[0:4]) # including 0 but not 4
print("2 ", fruit[1:4]) # including 1 but not 4
print("3 ", fruit[:5])
print("4 ", fruit[0:-3])
print("5 ", fruit[:len(fruit)-3])
print("6 ", fruit[-1:len(fruit) - 3]) # Empty as 4 (-1, last charachter position) to 2 is not possible by adding 1
print("7 ", fruit[-3:-1])

# Quick Quiz:
nm = "Harry"
print(nm[-4:-2])