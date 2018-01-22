import random
import string

print("Welcome to Hangman: Harry Potter Edition!")
word_list = ["Harry Potter", "Ron Weasley", "Hermione Granger", "Albus Dumbledore", "Severus Snape", "Remus Lupin",
            "Fred and George Weasley", "Neville Longbottom", "Xenophilius Lovegood", "Lord Voldemort"]

random_word = random.choice(word_list)
print(*random_word)
"""

A general guide for Hangman
1. Make a word bank - 10 items (DONE)
2. Pick an item from the list (DONE)
3. Hide the word (use *)
4. Reveal letters already guessed
5. Create the win condition

"""