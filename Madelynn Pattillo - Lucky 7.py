import random

print("Welcome to Lucky 7s!")
money = 15
print("You are starting with $15.")
rounds_played = 0
most_money = 0

while money > 0:
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    rolled = dice1 + dice2
    print("You bet $1.")
    rounds_played += 1
    money -= 1
    print("You now have %d dollars left." % money)
    print(rolled)

    if rolled == 7:
        money += 5
        print("You rolled a seven. You earn your bet plus an additional $4.")
        print("You now have %d dollars left." % money)

    if rolled != 7:
        print("You lost the bet.")

    if money >= most_money:
        most_money = money - most_money

    if money == 0:
        print("Game over! You now have $0 and played a total of %d rounds." % rounds_played)



# find greatest amount of money earned, round that you had the most money
