import random

def check(comp, user):
  if comp ==user:
    return 0
    
  if(comp == 0 and user ==1):
    return -1
    
  if(comp == 1 and user ==2):
    return -1
    
  if(comp == 2 and user == 0):
    return -1

  return 1
    
  
comp = random.randint(0, 2)
user = int(input("0 for Snake, 1 for water and 2 for Gun:\n"))

score = check(comp, user)

print("You: ", user)
print("Computer: ", comp)

if(score == 0):
  print("Its a draw")
elif (score == -1):
  print("You Lose")
else:
  print("You Won")
  


# My solution

#                S W G
# player =       0 1 2
# computer= S  0 D W L
#           W  1 L D W
#           G  2 W L D
import random as r
print("Welcome to Snake-Water-Gun Game!")
outcomes = [[0, 1, -1], [-1, 0, 1], [1, -1, 0]]
print("Game Points are:\nPlayer: 0 Computer: 0","\nRules are:\nSnake: 0 Water: 1 Gun: 2")
player = int(input("Please enter your move! \n"))
computer = r.randint(0, 2)
computerPoints = 0
playerPoints = 0
while player != 9:
    print(f"Player {player} Computer {computer}")
    if player not in [0, 1, 2]:
        print("Invalid Input!")
    elif outcomes[player][computer] == 0:
        print("Match Draw!")
    elif outcomes[player][computer] == -1:
        print("Lose!")
        computerPoints += 1
    elif outcomes[player][computer] == 1:
        playerPoints += 1
        print("Win!")
    
    computer = r.randint(0, 2)
    print(f"\nThe scores are: Computer {computerPoints} Player {playerPoints} \n")
    player = int(input("Please enter your move!\n"))

print(f"Final score for the game are: \nPlayer: {playerPoints} Computer: {computerPoints}")