# Hangman project (Day 7)

import random
'''STEP 1: GENERATE RANDOM WORD'''
game_over = False
word_list = ["ardvark", "baboon", "camel"]
word = random.choice(word_list)

'''STEP 2: GENERATE AS MANY BLANKS IN THE WORD'''
# create empty list
display = []    

# for each letter in the word, add '-' 
for letter in word:
    display.append("-")
print(display)

while not game_over:
    prompt = input("Guess a letter: ").lower()

    for position in range(len(word)):
        letter = word[position]
        if prompt == letter: 
            display[position] = letter
    print(display)
    '''STEP 3: CHECK IF PLAYER HAS WON'''
    if "-" not in display:
        game_over = True
    
print("You win")
