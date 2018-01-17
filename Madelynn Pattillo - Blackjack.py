import random

print("Welcome to Blackjack!")
player_card1 = random.randint(1, 10)
player_card2 = random.randint(1, 10)
player_cards = player_card1 + player_card2
blackjack = 21


def play(player_card1, player_card2, player_cards):
    if play_choice == "hit":
        player_card3 = random.randint(1, 10)
        player_card4 = random.randint(1, 10)
        player_cards = player_card1 + player_card2 + player_card3 + player_card4
        print(player_card3)
        print(player_card4)
        print("Your cards total to %d." % player_cards)
        dealer_card1 = random.randint(1, 10)
        dealer_card2 = random.randint(1, 10)
        dealer_cards = dealer_card1 + dealer_card2
        print("The dealer's cards total to %d." % dealer_cards)
    else:
        dealer_card1 = random.randint(1, 10)
        dealer_card2 = random.randint(1, 10)
        dealer_cards = dealer_card1 + dealer_card2
        print(dealer_card1)
        print(dealer_card2)
        dealer_cards = dealer_card1 + dealer_card2
        print("The dealer's cards total to %d." % dealer_cards)


def winner(dealer_cards, player_cards):
    if dealer_cards > player_cards:
        print("You lost. The dealer won!")
    elif dealer_cards > player_cards and dealer_cards > 21:
        print("You won!")
    elif player_cards > dealer_cards:
        print("You won!")
    elif player_cards > dealer_cards and player_cards > 21:
        print("You lost. The dealer won!")
    elif dealer_cards == blackjack and player_cards != blackjack:
        print("You lost. The dealer won!")
    elif player_cards == blackjack and dealer_cards != blackjack:
        print("You won!")
    elif player_cards == dealer_cards:
        print("It's a draw.")
    elif player_cards == blackjack:
        print("You won!")
    elif dealer_cards == blackjack:
        print("You lost. The dealer won!")


while player_cards <= 21:
    player_card1 = random.randint(1, 10)
    player_card2 = random.randint(1, 10)
    player_cards = player_card1 + player_card2
    dealer_card1 = random.randint(1, 10)
    dealer_card2 = random.randint(1, 10)
    dealer_cards = dealer_card1 + dealer_card2
    print(player_card1)
    print(player_card2)
    print("Your cards total to %d." % player_cards)
    play_choice = input("Do you want to stand or hit on your cards?")
    print(play_choice)
    print(play(player_card1, player_card2, player_cards))
    print(winner(dealer_cards, player_cards))
