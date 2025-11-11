marks = [12, 56, 32, 98, 12,  45, 1, 4]

# index = 0
# for mark in marks:
#   print(mark)
#   if(index == 3):
#     print("Harry, awesome!")
#   index +=1

for v in enumerate(marks, start=1):
  print(v[1])
  if(v[0] == 3):
    print("Harry, awesome!")