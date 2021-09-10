# Hangman project (Day 7)

import random
'''STEP 1: GENERATE RANDOM WORD'''
word_list = ["ardvark", "baboon", "camel"]
word = random.choice(word_list)

prompt = input("Guess a letter: ").lower()
for letter in word:
    if prompt == letter: 
        print("correct")
    else: 
        print("incorrect")

