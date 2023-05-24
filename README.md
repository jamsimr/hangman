# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

The file milestone_2.py contains a list of 5 words, generates a random word for that list and prints the word. The script asks for the user to an input a character, and checks that the character is a single letter, generating a response if valid.

The file milestone_3.py contains the script from milestone_2.py, called check_guess, and includes an additional script for the user to an input a character called ask_for_input, and checks that the character is a single letter, generating a response if valid in a while loop. check_guess is run in ask_for_input.


The file milestone_4.py creates the Hangman class and assigns the following attributes:
- word: The word to be guessed, picked randomly from the word_list. Remember to import the random module into your script.
- word_guessed: list - A list of the letters of the word, with for each letter not yet guessed. For example, if the word is 'apple', the word_guessed list would be ['', '', '', '', '']. If the player guesses 'a', the list would be ['a', '', '', '', ''].
- num_letters: int - The number of UNIQUE letters in the word that have not been guessed yet.
- num_lives: int - The number of lives the player has at the start of the game.
- word_list: list - A list of words.
- list_of_guesses: list - A list of the guesses that have already been tried. Set this to an empty list initially.
A list of Hangman pictures has been added that will generate a picture depedning on the amount of lives the player has left. An attempt to create a loop of the game was attempted with word_generator.

The file milestone_5.py includes the Hangman class from milestone_4.py and adds a function to allow for the game to be played.

