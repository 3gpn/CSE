import random

print("Welcome to Blackjack!")
Dealer_card1 = random.randint(1, 13)
Dealer_card2 = random.randint(1, 13)
Player_card1 = random.randint(1, 13)
Player_card2 = random.randint(1, 13)
blackjack = 21
Player_cards = Player_card1 + Player_card2
Dealer_cards = Dealer_card1 + Dealer_card2


def winner(Dealer_cards, Player_cards):
    if Dealer_cards > Player_cards and Dealer_cards < 21:
        print("You lost. The dealer won!")
    elif Dealer_cards > Player_cards and Dealer_cards > 21:
        print("You won!")
    elif Player_cards > Dealer_cards and Player_cards < 21:
        print("You won!")
    elif Player_cards > Dealer_cards and Player_cards > 21:
        print("You lost. The dealer won!")
    elif Dealer_cards == blackjack and Player_cards != blackjack:
        print("You lost. The dealer won!")
    elif Player_cards == blackjack and Dealer_cards != blackjack:
        print("You won!")
    elif Player_cards == Dealer_cards:
        print("It's a draw.")
    elif Player_cards == blackjack:
        print("You won!")
    elif Dealer_cards == blackjack:
        print("You lost. The dealer won!")


while Player_cards < 21:
    print(Player_card1)
    print(Player_card2)
    print("Your cards total to %d." % Player_cards)
    play_choice = input("Do you want to stand or hit on your cards?")
    print(play_choice)

    if play_choice == "hit":
        Player_card3 = random.randint(1, 13)
        Player_card4 = random.randint(1, 13)
        Player_cards = Player_card3 + Player_card4
        print(Player_card3)
        print(Player_card4)
        print("Your cards total to %d." % Player_cards)
    else:
        print(Dealer_card1)
        print(Dealer_card2)
        Dealer_cards = Dealer_card1 + Dealer_card2
        print("The dealer's cards total to %d." % Dealer_cards)
        print(winner(Dealer_cards, Player_cards))
