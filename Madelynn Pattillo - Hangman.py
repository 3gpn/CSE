import random
import string

print("Welcome to Hangman: Harry Potter Edition!")
guesses_left = 10
letters_guessed = [' ']
alphabet = string.ascii_letters
word_list = ["Harry Potter", "Ron Weasley", "Hermione Granger", "Albus Dumbledore", "Severus Snape", "Remus Lupin",
            "Fred and George Weasley", "Neville Longbottom", "Xenophilius Lovegood", "Lord Voldemort"]
random_word = random.choice(word_list)
while guesses_left >= 0:
    output = []
    for letter in random_word:
        if letter in letters_guessed:
            output.append(letter)
        elif letter.lower() in letters_guessed:
            output.append(letter)
        elif letter.upper() in letters_guessed:
            output.append(letter)
        else:
            output.append("*")
    guessed_word = "".join(output)
    print(guessed_word)

    if guessed_word == random_word:
        print("You win! The correct word is %s. Thanks for playing!" % random_word)
        exit(0)
    guess = input("Guess a letter from the alphabet. You have %d guesses left." % guesses_left)
    letters_guessed.append(guess)

    if guess not in random_word:
        guesses_left -= 1
    elif guess == alphabet:
        guesses_left -= 1

    print("You have guessed %s." % letters_guessed)
