a = input("Enter any value between 5 and 9 ")

if(a == "quit"):
    pass
elif(int(a)<5  or int(a)>9):
  raise  ValueError("Value should be between 5 and 9")
# elif 4<int(a)<10:
#      print("Correct Input!")

elif(4<int(a)<10):
   print("Correct input!")
else:
  raise Exception("Wrong Input!")
