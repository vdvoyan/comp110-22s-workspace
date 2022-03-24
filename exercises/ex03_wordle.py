"""Structured Wordle"""

__author__: str = "730518639"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(a: str, b: str):
    """Two string inputs, checks if b is contained in a."""
    assert len(b) == 1
    if a.__contains__(b):
        return True
    else:
        return False


def emojified(guess: str, secret: str):
    """Checks color of boxes for given guess and secret."""
    assert len(guess) == len(secret)
    for i in range(0, len(secret) - 1):
        if guess[i] == secret[i]:
            print(GREEN_BOX, end=' ')
        else:
            guess[i] != secret[i]
            print(WHITE_BOX, end=' ')
        if guess[i].__contains__(secret[i]):
            print(YELLOW_BOX, end=' ')


def input_guess(x: int) -> str:
    """Given a number for length, checks for the word to be of the same length."""
    word: str = input("Enter a 5 character word:")
    while len(word) != x:
        word: str = input("That was not 5 letters! Try again:")
    else:
        exit()


def main() -> None:
    """The entrypoint of the program and main game loop."""