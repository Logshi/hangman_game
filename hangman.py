import random
import time

# Welcoming the user
name = input("What is your name? ")
print("Hello, " + name + ", Time to play hangman!")

# Wait for 1 second
time.sleep(1)
print("Start guessing...")
time.sleep(0.5)

# Hangman stages
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
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
 /|\ |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\ |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\ |
 / \ |
      |
=========''']

# List of possible words
word_list = ["aardvark", "baboon", "camel", "jazz", "grass", "follow", "castle", "cloud"]
chosen_word = list(random.choice(word_list))

# Creates a variable with an empty value for the guesses
blank_list = ["_"] * len(chosen_word)
guesses = ''

# Determine the number of turns
turns = 6
update_display = 0

# Function to process a guess
def making_a_guess(guess, chosen_word, blank_list):
    correct_guess = False
    for x, letter in enumerate(chosen_word):
        if guess == letter:
            blank_list[x] = guess
            correct_guess = True
    return correct_guess

# Function to display the current state of the game
def display_hangman():
    print(HANGMANPICS[update_display])
    print(''.join(blank_list))

# Main game loop
print("Welcome to Hangman!")
display_hangman()

while update_display < turns:
    guess = input("Make a guess: ").lower()

    # Validating the user's input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    # Checking if the letter has been guessed before
    if guess in guesses:
        print("You've already guessed that letter. Try again.")
        continue

    guesses += guess
    correct_guess = making_a_guess(guess, chosen_word, blank_list)

    if not correct_guess:
        print(f"There is no {guess}, sorry.")
        update_display += 1

    display_hangman()

    # Check if the player has won
    if blank_list == chosen_word:
        print("YOU WIN!")
        break

    # Check if the player has lost
    if update_display == turns:
        print("GAME OVER. The word was: " + ''.join(chosen_word))