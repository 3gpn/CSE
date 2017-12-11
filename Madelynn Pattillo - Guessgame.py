import random

num_of_guesses = 5


def compare(guess, num_of_guesses):
    if guess < num:
        num_of_guesses -= 1
        print("Try again...but possibly higher than the last... You have %d guesses left." % num_of_guesses)
    elif guess > num:
        num_of_guesses -= 1
        print("That's incorrect...maybe something lower next time... You have %d guesses left." % num_of_guesses)
    else:
        num_of_guesses -= 1
        print("That's correct! You had %d guesses left." % num_of_guesses)


print("Welcome to Guessgame!")
num = random.randint(1, 50)

print()

if num_of_guesses == 0:
    print("I'm sorry but that's incorrect. No more chances for you! Goodbye!")


while num_of_guesses <= 5:
    guess = input("Pick a number from 1 to 50.")
    compare(int(guess), num_of_guesses)
