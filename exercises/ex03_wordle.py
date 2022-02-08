"""EX03 - Wordle."""
__author__ = "730394362"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
result_guess: str = ""


def contains_char(searched_through: str, searched_for: str) -> bool:
    """Tells us if the character is found in the secret word by returning true or false."""
    assert len(searched_for) == 1
    index = 0
    while index < len(searched_through):
        if searched_through[index] == searched_for:
            return True
        else:
            index += 1
            # raises the index so the loop can continue until the whole word has been searched through for matching characters.
    return False


def emojified(guess_word: str, secret_word: str) -> str:
    """Returns an emoji string that informs the player whether the characters of their guess are in the correct places using the contains_char function to search through the inputs."""
    assert len(guess_word) == len(secret_word)
    result_guess: str = ""
    index: int = 0
    while index < len(secret_word):
        if secret_word[index] == guess_word[index]:
            result_guess += GREEN_BOX
        elif contains_char(secret_word, guess_word[index]) is True:
            result_guess += YELLOW_BOX
            # calling the contains_char function checks the function for character matches with the secret word and returns a bool value, which we then use to create conditions for emojified function to spit out strings of boxes that codfies the guessed word and informs the player about the placement of characters in their guess
        else:
            result_guess += WHITE_BOX
        index += 1
    return result_guess


def input_guess(exp_length: int) -> str:
    """Continues to prompt user for a guess matching the expected length of the given integer parameter."""
    input_guess: str = input(f"Enter a {exp_length} character word: ")
    while len(input_guess) != exp_length:
        input_guess = input(f"That wasn't {exp_length} chars! Try again: ")
        # while loop will continue to prompt the user until the correct number of characters are given in a guess, then the function returns the guessed word back to the player; we use this in later functions to check if the input_guess matches the secret word.
    return input_guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    turns: int = 1
    won: bool = False
    secret_word: str = "codes"
    while turns <= 6 and won is False:
        print(f"=== Turn {turns}/6 ===")
        guess: str = input_guess(len(secret_word))
        # assigning a variable to the input_guess function so that it can keep prompting the player, store the player's input into that function, and then compare it to the secret word.
        if guess != secret_word:
            print(emojified(guess, secret_word))
            turns += 1
            # if the guessed word does not equal the secret word, it prints the codified boxes to help give the player hints, and also increases the turns so that loop can continue and the player can keep guessing.
        elif guess == secret_word:
            print(emojified(guess, secret_word))
            print(f"You won in {turns}/6 turns!")
            won = True
            # if the player's guess matches the secret word, it prints the codified response using the emojified function and informs the player of their win in how many turns it took them.
    if turns > 6:
        print("X/6 - Sorry, try again tomorrow!")
        # once the player exceeds six turns, they are kicked out of the game


if __name__ == "__main__":
    main()