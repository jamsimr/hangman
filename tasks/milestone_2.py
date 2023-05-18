import random

word_list = ["pear", "banana", "blueberry", "date", "mango"]

def choice():
    return random.choice(word_list)

word = choice()

print(word)

guess = input("Type the letter of your guess: ")

if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    "Oops! That is not a valid input."