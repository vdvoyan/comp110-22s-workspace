SECRET: int = 5
SECRET_A: int = 4
SECRET_B: int = 3
SECRET_C: int = 2
SECRET_D: int = 1
SECRET_E: int = 0


user_name: str = input("What is your name? ")
print("Hello, " + user_name)

mixed_list = ['5-Great', '4-Good', '3-OK', '2-Alright', '1-Not Good', '0-Bad']
print(mixed_list)

guess: int = int(input("How is your day?"))

if guess == SECRET:
    print("That's great!")
else:
    if guess == SECRET_A:
        print("Sounds good!")
    if guess == SECRET_B:
        print("Everything's OK! Hope you feel better!")
    if guess == SECRET_C:
        print("Everything will be alright! Hope you feel better!")
    if guess == SECRET_D:
        print("It will improve soon! Hope you feel better!")
    if guess == SECRET_E:
        print("Sorry to hear that :( Hope you feel better!")

print("You are amazing, " + user_name + "!")
print("Don't stop smiling!")
print("Talk to Vahan and your day will become ecstatic!")