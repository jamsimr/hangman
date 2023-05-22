#%%
def check_guess(guess):
    lowercase_guess = guess.lower()
    if lowercase_guess in word:
        print(f"Good guess! {guess} in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again")

def ask_for_input():
    while True:
        guess = input("Type a letter: ")
        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    return check_guess(guess)

word = "apple"

ask_for_input()
# %%
