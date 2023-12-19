import random

#random num variable and lives variable
random_number = random.randint(0, 100)
lives = 3

#Welcome message
print('''Welcome to the number guessing game!
The rules are simple: Guess the random number.\n''')

#debug printing of the number
print(f"Debug: {random_number}")

#Provides player hint on whether number is greater or less than 50
def high_low():
    if random_number > 50:
        print("Hint: The number is greater than 50.")
    elif random_number >= 50 and random_number <= 60:
        print("Hint: It's somewhere in the middle")
    else:
        print("Hint: The number is less that 50.")

high_low()

user_guess = int(input("Enter a number between 1 - 100: "))

#Defines function and creates variable flag to determine whether the user guess is the random number or not. If yes - Player wins Else - lose life and guess again
def right_wrong():
    global guessed_correctly

    if user_guess == random_number:
        print("That was the correct number. You Win!")
        guessed_correctly = True
        exit()
    else:
        global lives
        lives -= 1
        print(f"Incorrect. You have: {lives} lives remaining.\n")

#Variable flag
guessed_correctly = False

#Defines function for if lives reach 0 then tells the player they are out of lives and ends the game.
def no_lives():
    if lives < 1:
        print(f"Game Over! The number was: {random_number}")
        exit()


#While loop that continues unit the user guesses the random number 
while not guessed_correctly:
    #Calls right_wrong, high_low, and no_lives functions
    right_wrong()
    high_low()
    no_lives()
    user_guess = int(input("Enter a number between 1 - 100: "))
    

    
    