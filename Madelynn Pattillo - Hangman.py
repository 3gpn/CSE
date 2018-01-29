import random
import string

print("Welcome to Hangman: Harry Potter Edition!")
guesses_left = 10
letters_guessed = [' ']
alphabet = string.ascii_letters
word_list = ["Harry Potter", "Ron Weasley", "Hermione Granger", "Albus Dumbledore", "Severus Snape", "Remus Lupin",
            "Fred and George Weasley", "Neville Longbottom", "Xenophilius Lovegood", "Lord Voldemort"]
random_word = random.choice(word_list)

while guesses_left > 0:
    output = []
    for letter in random_word:
        if letter in letters_guessed:
            output.append(letter)
        else:
            output.append("*")
    print(output)
    guessed_word = "".join(output)
    guess = input("Guess a letter from the alphabet. You have %d guesses left." % guesses_left)

    if guess.lower() in random_word and alphabet:
        output.append(guess.lower())
        guesses_left -= 1

    letters_guessed.append(guess)
    print("You have guessed %s." % letters_guessed)

    # if random_word == guessed_word:
    #     exit(0)
    #     print("Game over!")
# 5. Create the win condition
