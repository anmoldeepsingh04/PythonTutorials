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