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
            # raises the index so the loop can continue until the whole word has been searched through.
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
            # calling the contains_char function checks the function for character matches and returns a bool value, which we then use to create conditions for emojified function to spit out strings of boxes that codfies the guessed word and informs the player about the placement of characters in their guess
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
    while turns <= 6 and won is False:
        print(f"=== Turn {turns}/6 ===")
        secret_word: str = "codes"
        exp_length: int = len(secret_word)
        emojified(input_guess(exp_length), secret_word)
        if input_guess == secret_word:
            won: bool = True
            emojified(input_guess(exp_length), secret_word)
            print(f"You won in {turns}/6 turns!")
            print(result_guess)
        else:
            emojified(input_guess(exp_length), secret_word)
            print(result_guess)
            turns += 1
        print("X/6 - Sorry , try again tomorrow!")


if __name__ == "__main__":
    main()


        
