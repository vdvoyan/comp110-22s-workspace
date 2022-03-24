"""One Shot Wordle"""

__author__ = "730518639"


secret: str = "python"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

word: str = input("What is your 6-letter guess?")

while len(word) != 6:
    word: str = input("That was not 6 letters! Try again:")
    if word == secret:
        print("\nWoo! You got it!")
        break
    if len(word) == 6:
        break

for i in range(0, 6):
    while word[i] == secret[i]:
        print(GREEN_BOX, end=' ')
        break
    if word[i] != secret[i]:
        print(WHITE_BOX, end=' ')
    

if word == secret:
    print("\nWoo! You got it!")
    exit()

if len(word) == 6:
    print("\nNot quite. Play again soon!")