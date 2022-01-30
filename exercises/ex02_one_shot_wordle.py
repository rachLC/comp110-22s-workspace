"""EX02 - One-Shot Wordle- Loops!"""
__author__ = "730394362"
secret_word = str("python")
l: int = len(secret_word)
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
guess_input = input(f"What is your {l}-letter guess?")
while len(guess_input) != len(secret_word):
    guess_input = input(f"That was not {l} letters! Try again: ")
index: int = 0
# index variable is used to keep track of what index we are checking in the guess_input word
result_guess: str = ""
# the empty string is established so we can concatenate the emojis generated from comparing the indices of the guess_input and secret_word with the variable result_guess
while index < len(secret_word):
    if guess_input[index] == secret_word[index]:
        result_guess += GREEN_BOX
        # due to the way indices are numbered starting at 0, the numerical length of the secret word will always be greater than the index being checked. So, while the index is less than the length of the word, we ensure that there are actual characters in the indices we are checking. 
        # the equalizing statement between guess_input[index] and secret_word[index] checks to see if characters in guess_input at the current index are the same as the characters in secret_word in the same index, which hints to players if the characters in the guesses are in the correct location.
        # when the characters in the indices match, a str representing the green emoji is added to the empty result_guess str to visually signal players that characters of their guess are in the correct index.
    else:
        any_matches = False 
        alt_indices: int = 0
        # creating a variable to track the other indices we are checking after confirming that the same indices between guess_input and secret_word do not match, this is so we can see if certain characters in guess_input exist at any indices in secret_word at all.
        while alt_indices < len(secret_word):
            if secret_word[alt_indices] == guess_input[index]:
                any_matches = True
                # if character at the alternate index in guess_input are found at the current index in secret_word, then any_matches becomes true
            alt_indices += 1
            # if the character in a specific index does not match the character in the current index of the secret_word, then the alt_indices is increased by one so the process can be repeated at another index until all indices have been checked for matches and the loop ends.
        if any_matches is True:
            result_guess += YELLOW_BOX
            # if character at alternate indices of the guess_input are found in the indices of the secret_word, but not the same indices, then a yellow box emoji is added to result str to relay this to the player
        else:
            result_guess += WHITE_BOX
        # when none of the characters at any of the indices of the guess_input are found at any of the indices of the secret_word, a str representing the white box emoji is added to the result_guess empty str
    index += 1
    # increasing the index numerical value ensures the computer is not evaluating the same index forever, the computer circles back through the loop until the index number is equal to the length of the word, meaning there are no more characters to check, and the loop ends.
print(result_guess)
if guess_input != secret_word:
    print("Not quite. Play again soon!")
if guess_input == secret_word:
    print("Woo! You got it!")