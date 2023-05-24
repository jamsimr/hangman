import random

fruit = ["pear", "banana", "blueberry", "date", "mango"]

class Hangman:

    def __init__(self, word_list, num_lives=5) -> None:
        '''Defines the attributes necessary for the game to run'''
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word)) #Finds the unique letters in a word
        self.list_of_guesses = []

    def check_guess(self, guess):
        '''Checks that the user's input is valid, and if it is in the randomly generated word'''
        lowercase_guess = guess.lower()
        if lowercase_guess in self.word:
            print(f"Good guess! {guess} in the word.")
            for i, char in enumerate(self.word):
                if char == lowercase_guess:
                    self.word_guessed[i] = guess
            self.num_letters -= 1
        else:
            print(f"Sorry, {guess} is not in the word.")
            self.num_lives -= 1
            print(f"You have {self.num_lives} lives left.")
            self.print_hangman(self.num_lives)
        print(self.word_guessed)
        self.list_of_guesses.append(lowercase_guess)
        if self.num_lives == 0:
            print(f"The word was {self.word}")
            return

    def ask_for_input(self):
        '''Asks user for input'''
        while True:
            guess = input("Type a letter: ")
            if len(guess) != 1 and guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print(f"You already tried {guess}")
            else:
                self.check_guess(guess)
                break
    
    def print_hangman(self, num_lives):
        '''Generates a picture depending on how many lives are left'''
        if self.num_lives == 5:
            print("  ________")
            print(" |        |")
            print(" |        O")
            print(" |")
            print(" |")
            print(" |")
            print("_|_")
        elif self.num_lives == 4:
            print("  ________")
            print(" |        |")
            print(" |        O")
            print(" |        |")
            print(" |")
            print(" |")
            print("_|_")
        elif self.num_lives == 3:
            print("  ________")
            print(" |        |")
            print(" |        O")
            print(" |       /|")
            print(" |")
            print(" |")
            print("_|_")
        elif self.num_lives == 2:
            print("  ________")
            print(" |        |")
            print(" |        O")
            print(" |       /|\\")
            print(" |")
            print(" |")
            print("_|_")
        elif self.num_lives == 1:
            print("  ________")
            print(" |        |")
            print(" |        O")
            print(" |       /|\\")
            print(" |       /")
            print(" |")
            print("_|_")
        else:
            print("  ________")
            print(" |        |")
            print(" |        O")
            print(" |       /|\\")
            print(" |       / \\")
            print(" |")
            print("_|_")
    
def play_game(word_list):
    '''Runs Hangman Class as a game'''
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print(f"You lost the game")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
            break
        else:
            print("Congratulations. You won the game!")

play_game(fruit)
