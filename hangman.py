# Hangman project (Day 7)
'''STEP 5: INCREASE NUMBER OF WORDS USED'''
from words import words
import random
'''STEP 1: GENERATE RANDOM WORD'''
game_over = False
lives = 6
word = random.choice(words)

'''STEP 2: GENERATE AS MANY BLANKS IN THE WORD'''
# create empty list
display = []    

# for each letter in the word, add '-' 
for letter in word:
    display.append("-")
print(display)

while not game_over:
    prompt = input("Guess a letter: ").lower()

    if prompt in display:
        print(f"You already guessed {prompt} already")

    for position in range(len(word)):
        letter = word[position]
        if prompt == letter: 
            display[position] = letter
    print(display)
    '''STEP 4: DECREASE LIVES'''
    if prompt not in word:
        print("You lost a life")
        lives -= 1
        if lives == 0:
            print("Game over! You lose!")
            game_over = True
    '''STEP 3: CHECK IF PLAYER HAS WON'''
    if "-" not in display:
        game_over = True
        print("You win")

