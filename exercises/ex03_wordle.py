"""EX03 - Wordle."""

__author__ = "730433734"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(word: str, char: str) -> bool:
    """Return True if char is found at any index of word, and return False otherwise."""
    assert len(char) == 1
    i: int = 0
    while i < len(word):
        if word[i] == char:
            return True
        else:
            i += 1
    return False


def emojified(guess_word: str, secret_word: str) -> str:
    """Return a string of emoji whose color codifies the same as previously implemented in EX02."""
    assert len(guess_word) == len(secret_word)
    result: str = ""
    i: int = 0
    while i < len(secret_word):
        if secret_word[i] == guess_word[i]:
            result += GREEN_BOX
        elif contains_char(secret_word, guess_word[i]):
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
        i += 1
    return result


def input_guess(n: int) -> str:
    """Continue prompting users until they provide a guess of the expected length."""
    input_word: str = input(f"Enter a {n} character word: ")
    while True:
        if len(input_word) != n:
            input_word = input(f"That wasn't {n} chars! Try again: ")
        elif len(input_word) == n:
            return input_word


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    current_turn: int = 1
    won: bool = False
    while current_turn <= 6 and won is False:
        print(f"=== Turn {current_turn}/6 ===")
        guess_word = input_guess(len(secret_word))
        print(emojified(guess_word, secret_word))
        if guess_word == secret_word:
            print(f"You won in {current_turn}/6 turns!")
            won = True
        elif current_turn == 6:
            print("X/6 - Sorry, try again tomorrow!")
            current_turn += 1
        else:
            current_turn += 1


if __name__ == "__main__":
    main()