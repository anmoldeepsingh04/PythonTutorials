import string
import random
# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode
def secretMessage(normMessage):
    a = int(input("Do you want to encode or decode? \nPress 0 to Encode \nPress 1 to Decode \n"))
    if a == 0:
        if len(normMessage) > 2:
            normMessage = normMessage + normMessage[0]
            normMessage = normMessage[1:]
            normMessage = normMessage[::-1]
            front, back = ["",""]
            for i in range(0, 3):
                front = front + random.choice(string.ascii_letters)
                back = back + random.choice(string.ascii_letters)
            normMessage = front + normMessage + back
        else:
            normMessage = normMessage[::-1]
    
    elif a == 1:
        if len(normMessage) > 2:
            normMessage = normMessage[3:len(normMessage)-3]
            normMessage = normMessage[::-1]
            normMessage = normMessage[-1] + normMessage[:len(normMessage)-1]
        else:
            normMessage = normMessage[::-1]
    
    else:
        raise ValueError("Invalid Input!")
    return normMessage


message = "WguT!won yltcefrep gnikrow si sihVja"

print(secretMessage(message))