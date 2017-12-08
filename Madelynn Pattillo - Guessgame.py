import random


def compare(guess):
    if guess < num:
        print("Try again...but possibly higher than the last...")
    elif guess > num:
        print("That's incorrect...maybe something lower next time...")
    else:
        print("That's correct!")


print("Welcome to Guessgame!")
num = random.randint(1, 50)

print()
guess = input("Pick a number from 1 to 50.")
compare(int(guess))


num_of_guess = int
# 5. Add 5 guesses.
