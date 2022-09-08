"""EX02 - Wordle."""

__author__ = "730433734"

secret_word: str = "python" 
guess_word: str = input(f"What is your {len(secret_word)}-letter guess? ")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
i: int = 0
result: str = ""

"""When the lengths do not match"""
while len(guess_word) != len(secret_word):
    guess_word = input(f"That was not {len(secret_word)} letters! Try again: ")

"""When the lengths match"""
if guess_word != secret_word:
    while i < len(secret_word):
        if guess_word[i] == secret_word[i]:
            result += GREEN_BOX
        elif guess_word[i] != secret_word[i]:
            """When two characters do not match"""
            is_exist: bool = False
            j: int = 0
            while is_exist is False and j < len(secret_word):
                if guess_word[i] == secret_word[j]:
                    is_exist = True
                j += 1
            if is_exist is False:
                result += WHITE_BOX
            else:
                result += YELLOW_BOX
        i += 1
    print(result)
    print("Not quite. Play again soon!")
elif guess_word == secret_word:
    result = GREEN_BOX * len(secret_word)
    print(result)
    print("Woo! You got it!")