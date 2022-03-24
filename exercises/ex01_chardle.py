"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730518639"

word: str = input("Enter a 5-character word: ")

if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit()

letter: str = input("Enter a single character: ")

if len(letter) != 1:
    print("Error: Character must be a single character.")
    exit()

if letter in word:
    print("Searching for " + letter + " in " + word)
else:
    print("Searching for " + letter + " in " + word)
    print("No instances of", letter, "found in", word)
    exit()

index = word.index(letter)


for pos, char in enumerate(word):
    if char == letter:
        print(letter + " found at Index", pos)


def countX(word, x):  # Counts number of instances of a letter in the given word.
    count = 0
    for ele in word:
        if (ele == x):
            count = count + 1
    return count


x = letter

if countX(word, x) == 1:
    print(countX(word, x), "instance of", letter, "found in", word)
else:
    print(countX(word, x), "instances of", letter, "found in", word)