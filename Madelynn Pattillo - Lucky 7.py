import random

print("Welcome to Lucky 7s!")
money = 15
print("You are starting with $15.")
rounds_played = 0
most_money = 0
highest_round = 0

while money > 0:
    if most_money < money:
        most_money = money
        highest_round = rounds_played

    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    rolled = dice1 + dice2
    print("You bet $1.")
    rounds_played += 1
    money -= 1
    print("You now have $%d left." % money)
    print(rolled)

    if rolled == 7:
        money += 5
        print("You rolled a seven. You earn your bet plus an additional $4.")
        print("You now have $%d left." % money)
    else:
        print("You lost the bet.")

print("Game over! You now have $0 and played a total of %d rounds" % rounds_played)
print("At round %d, you had the most money: %d." % (highest_round, most_money))
