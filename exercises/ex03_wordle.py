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
        else:
            result_guess += WHITE_BOX
        index += 1
    return result_guess


def input_guess(exp_length: int) -> str:
    """Continues to prompt user for a guess matching the expected length of the given integer parameter."""
    while len(input(f"Enter a {exp_length} character word: ")) != exp_length:
        input_guess = input(f"That wasn't {exp_length} chars! Try again: ")
    return input_guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
