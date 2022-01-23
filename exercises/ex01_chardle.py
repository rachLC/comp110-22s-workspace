"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730394362"
number_char: int = 0
word_input: str = input("Enter a 5-character word:")
if len(word_input) > 5:
    print("Error: Word must contain 5 characters")
    exit()
if len(word_input) < 5:
    print("Error: Word must contain 5 characters")
    exit()
char_input: str = input("Enter a single character:")
if len(char_input) > 1:
    print("Error: Character must be a single character.")
    exit()
if len(char_input) < 1:
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + char_input + " in " + word_input + ".")
if char_input == word_input[0]:
    print(char_input + " found at index 0")
    number_char = number_char + 1
if char_input == word_input[1]:
    print(char_input + " found at index 1")
    number_char = number_char + 1
if char_input == word_input[2]:
    print(char_input + " found at index 2")
    number_char = number_char + 1
if char_input == word_input[3]:
    print(char_input + " found at index 3")
    number_char = number_char + 1
if char_input == word_input[4]:
    print(char_input + " found at index 4")
    number_char = number_char + 1
if number_char == 0:
    print("No instances of " + char_input + " found in " + word_input)
else: 
    print(str(int(number_char)) + " instances of " + char_input + " found in " + word_input)