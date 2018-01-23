import random
import string

print("Welcome to Hangman: Harry Potter Edition!")
guesses_left = 10
letters_guessed = []
word_list = ["Harry Potter", "Ron Weasley", "Hermione Granger", "Albus Dumbledore", "Severus Snape", "Remus Lupin",
            "Fred and George Weasley", "Neville Longbottom", "Xenophilius Lovegood", "Lord Voldemort"]
random_word = random.choice(word_list)

while guesses_left > 0:
    guess = input("Guess a letter from A to Z. You have %d guesses left." % guesses_left)
    letters_guessed.append(guess)
    print("You have guessed %s." % letters_guessed)
    guesses_left -= 1

"""

A general guide for Hangman
1. Make a word bank - 10 items (DONE)
2. Pick an item from the list (DONE)
3. Add a guess to the list of letters guessed (DONE)
4. Reveal letters already guessed
5. Create the win condition

"""