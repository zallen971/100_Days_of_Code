import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False
word_list = ["serendipity", "ephemeral", "quibble", "gumption", "nostalgia", "impromptu", "tapestry"]
random_word = random.choice(word_list)
word_length = len(random_word)
lives = 6
display = []
guessed_letters = " "

print(''' Welcome to
    888                                                           
    888                                                           
    888                                                           
    88888b.  8888b. 88888b.  .d88b. 88888b.d88b.  8888b. 88888b.  
    888 "88b    "88b888 "88bd88P"88b888 "888 "88b    "88b888 "88b 
    888  888.d888888888  888888  888888  888  888.d888888888  888 
    888  888888  888888  888Y88b 888888  888  888888  888888  888 
    888  888"Y888888888  888 "Y88888888  888  888"Y888888888  888 
                                888                              
                            Y8b d88P                              
                             "Y88P"                               
      ''')

print(f"Debugging: {random_word}")


for _ in range(word_length):
    display += "_"
    
print(display)


while not end_of_game:
    print(f"You currently have: {lives} lives")
    guess = input("Please guess a random letter: \n")


    for position in range(word_length):
        letter = random_word[position]
        if letter == guess:
            display[position] = letter


        if "_" not in display:
            end_of_game = True
            print(f"The word was: {random_word}. You Win!")

    if guess not in random_word:
            lives -= 1
            print(f"You have: {lives} left")
            print(stages[lives])
            if lives == 0:
                print("You lose!")
                break

    
    if guess not in random_word and guess not in guessed_letters:
         guessed_letters += f" {guess}"
    
    print(f"Already guessed letters: {guessed_letters}")
    
    print(f"{' '.join(display)}\n")