# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

The file milestone_2.py contains a list of 5 words, generates a random word for that list and prints the word. The script asks for the user to an input a character, and checks that the character is a single letter, generating a response if valid.

The file milestone_3.py contains the script from milestone_2.py, called check_guess, and includes an additional script for the user to an input a character called ask_for_input, and checks that the character is a single letter, generating a response if valid in a while loop. check_guess is run in ask_for_input.