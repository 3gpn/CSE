import random

num_of_guesses = 5


def compare(guess, num_of_guesses):
    if guess < num:
        num_of_guesses -= 1
        print("Try again...but possibly higher than the last... You have %d guesses left." % num_of_guesses)
        guess = input("Try again.")
    elif guess > num:
        num_of_guesses -= 1
        print("That's incorrect...maybe something lower next time... You have %d guesses left." % num_of_guesses)
        guess = input("Try again.")
    else:
        num_of_guesses -= 1
        print("That's correct! You had %d guesses left." % num_of_guesses)


print("Welcome to Guessgame!")
num = random.randint(1, 50)

print()
guess = input("Pick a number from 1 to 50.")
compare(int(guess), num_of_guesses)

if num_of_guesses == 0:
    print("I'm sorry but that's incorrect. No more chances for you! Goodbye!")
