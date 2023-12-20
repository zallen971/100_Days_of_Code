import random


#The choices
choices = ["Rock", "Paper", "Scissors"]


#Store player choice in a variable
player_choice = ""

#While player choice isn't Rock, Paper, or Scissors
while player_choice not in choices:
    player_choice = input("Rock, Paper, or Scissors: ")

    if player_choice not in choices:
        print("Error in choice, please pick again....")
        continue
    else:
        break


#Store computer choice in a variable
computer_choice = random.choice(choices)

#Prints both the players choice and computers choice
print(f''' 
    Player Chose: {player_choice} 
    Computer Chose: {computer_choice}\n''')


#If statement to determin who wins the game and prints the winner.
if player_choice == computer_choice:
    print("It's a tie!")
elif player_choice == "Rock":
    if computer_choice == "Paper":
        print("Computer Wins!")
    else:
        print("Player Wins!")
elif player_choice == "Paper":
    if computer_choice == "Scissors":
        print("Computer Wins!")
    else:
        print("Player Wins!")
elif player_choice == "Scissors":
    if computer_choice == "Rock":
        print("Computer Wins!")
    else:
        print("Player Wins!")
else:
    print("It's a Tie!")

