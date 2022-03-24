"""Program that reverses any given integer."""

__author__: str = "730518639"


number: int = int(input("Input any number: "))

r_number: int = 0

while (number > 0):
    rem: int = number % 10
    r_number = r_number * 10 + rem
    number = number // 10

print(r_number)