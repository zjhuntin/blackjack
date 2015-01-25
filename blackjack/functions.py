from card import Card
from interface import*


def checker_for_letters(prompt):
    """Way to check to make sure that the player is inputting any input that
    requires letters."""
    response = input(prompt)
    response = response.upper()
    if mode == "":
        print("You entered nothing, please try again.")
        return checker_for_words()
    if len(response) > 1:
        print("You entered more than one character. Please try again.")
        return checker_for_words()
    if not response.isalpha():
        print("You did not enter a letter, please try again.")
    return response


def check_bust(hand):
    """Returns True if the value of the hand is greater than 21. False if it
    is less than 21."""
    return hand.value > 21


def blkjck_chk(hand):
    """Returns True if the hand was blackjack."""
    if hand.value == 21 and len(hand) == 2:
         return True
    else:
        return False

def check_for_insurance(side_bet, dealer_hand, player_money):
    """This checks to see if the player betted for insurance. and that the
    dealer has blackjack. If they do it pays out double the bet to the
    player. Otherwise they lose the bet."""
    if side_bet > 0 and blkjck_chk(dealer_hand):
        won_insurance_bet(side_bet)
        player_money += (side_bet * 2)
    elif side_bet > 0 and not blkjck_chk(dealer_hand):
        lost_insurance_bet(side_bet)

def is_ace(dealer_hand):
    return dealer_hand.value == 11


def hit(player_or_dealer, deck):
    player_or_dealer.take_card(deck)

# def decider(choice, player, deck):
#     if choice = "H":
#         return hit(player, deck)
#     if choice = "S":
#         return stand = True
