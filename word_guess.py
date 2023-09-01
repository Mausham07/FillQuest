# This is the word_guesser code.

import random # importing random for use

# Print the welcome
print("\nWelcome to the WORD GUESSER game.\n")
print("Please Guess the word that fill the given blanks\n")

# random words in list
random_words = [
    "apple", "banana", "orange", "strawberry", "mango", "lemon",
    "car", "bicycle", "bus", "motorcycle", "airplane", "boat",
    "usa", "france", "japan", "australia", "brazil", "india",
    "emily", "daniel", "sophia", "liam", "olivia", "ethan",
    "pizza", "burger", "sushi", "pasta", "ice cream", "chocolate",
    "elephant", "lion", "giraffe", "dolphin", "kangaroo", "penguin"
]

# hangman 
lives = ['''
+---+
 |  |
 O  |
/|\ |
/ \ |
    |
======
''', '''
+---+
 |  |
 O  |
/|\ |
/   |
    |
======
''', '''
+---+
 |  |
 O  |
/|\ |
    |
======
''', '''
+---+
 |  |
 O  |
/ \ |
    |
======
''', '''
+---+
 |  |
 O  |
    |
    |
======
''', '''
+---+
 |  |
    |
    |
    |
======
''']

set_of_lives = 6
# Randomly chose a word from the random_words 
random_word = random.choice(random_words)

# create a blanks as length of the random_word
blanks = []
for _ in range(len(random_word)):
    blanks += "_"

# ask user to guess the letter
# user_letter = input("\nPlease guess a letter: ").lower()

while ("_" in blanks) and (set_of_lives > 0): 
    print(f"{' '.join(blanks)}")
    a_life = lives[set_of_lives]
    print(a_life)
    user_letter = input("\nPlease guess a letter: ").lower()
    if not user_letter in random_word:
      print("\nYou lost life. Please guess again.")  
      set_of_lives = set_of_lives - 1
    else:
        # Check if the user guessed letter match with letter inside random word.
        for index in range(len(random_word)):
            letter = random_word[index]
            if user_letter == letter:
                blanks[index] = letter # change the blanks by the user guessed letter if matched

if "_" not in blanks:
    print("You won")
else:
    print("You loose")