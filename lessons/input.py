"""Using input"""


SECRET: int = 1

user_name: str = input("What is your name? ")
print("Hello, " + user_name)
guess: int = int(input("How is your day? 1 - good, 0 - bad."))

if guess == SECRET:
    print("That's great!")
else:
    print("Hope you feel better!")

print("You are amazing, " + user_name + "!")