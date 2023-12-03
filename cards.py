# cards.py
import random
from enum import Enum

class PlayingCard(Enum):
    ACE_OF_CLUBS = (1, 'ace_of_clubs')
    ACE_OF_DIAMONDS = (1, 'ace_of_diamonds')
    ACE_OF_HEARTS = (1, 'ace_of_hearts')
    ACE_OF_SPADES = (1, 'ace_of_spades')
    TWO_OF_CLUBS = (2, 'two_of_clubs')
    TWO_OF_DIAMONDS = (2, 'two_of_diamonds')
    TWO_OF_HEARTS = (2, 'two_of_hearts')
    TWO_OF_SPADES = (2, 'two_of_spades')
    THREE_OF_CLUBS = (3, 'three_of_clubs')
    THREE_OF_HEARTS = (3, 'three_of_hearts')
    THREE_OF_DIAMONDS = (3, 'three_of_diamonds')
    THREE_OF_SPADES = (3, 'three_of_spades')
    FOUR_OF_CLUBS = (4, 'four_of_clubs')
    FOUR_OF_DIAMONDS = (4, 'four_of_diamonds')
    FOUR_OF_HEARTS = (4, 'four_of_hearts')
    FOUR_OF_SPADES = (4, 'four_of_spades')
    FIVE_OF_CLUBS = (5, 'five_of_clubs')
    FIVE_OF_DIAMONDS = (5, 'five_of_diamonds')
    FIVE_OF_HEARTS = (5, 'five_of_hearts')
    FIVE_OF_SPADES = (5, 'five_of_spades')
    SIX_OF_CLUBS = (6, 'six_of_clubs')
    SIX_OF_DIAMONDS = (6, 'six_of_diamonds')
    SIX_OF_HEARTS = (6, 'six_of_hearts')
    SIX_OF_SPADES = (6, 'six_of_spades')
    SEVEN_OF_CLUBS = (7, 'seven_of_clubs')
    SEVEN_OF_DIAMONDS = (7, 'seven_of_diamonds')
    SEVEN_OF_HEARTS = (7, 'seven_of_hearts')
    SEVEN_OF_SPADES = (7, 'seven_of_spades')
    EIGHT_OF_CLUBS = (8, 'eight_of_clubs')
    EIGHT_OF_DIAMONDS = (8, 'eight_of_diamonds')
    EIGHT_OF_HEARTS = (8, 'eight_of_hearts')
    EIGHT_OF_SPADES = (8, 'eight_of_spades')
    NINE_OF_CLUBS = (9, 'nine_of_clubs')
    NINE_OF_DIAMONDS = (9, 'nine_of_diamonds')
    NINE_OF_HEARTS = (9, 'nine_of_hearts')
    NINE_OF_SPADES = (9, 'nine_of_spades')
    TEN_OF_CLUBS = (10, 'ten_of_clubs')
    TEN_OF_DIAMONDS = (10, 'ten_of_diamonds')
    TEN_OF_HEARTS = (10, 'ten_of_hearts')
    TEN_OF_SPADES = (10, 'ten_of_spades')
    JACK_OF_CLUBS = (10, 'jack_of_clubs')
    JACK_OF_DIAMONDS = (10, 'jack_of_diamonds')
    JACK_OF_HEARTS = (10, 'jack_of_hearts')
    JACK_OF_SPADES = (10, 'jack_of_spades')
    QUEEN_OF_CLUBS = (10, 'queen_of_clubs')
    QUEEN_OF_DIAMONDS = (10, 'queen_of_diamonds')
    QUEEN_OF_HEARTS = (10, 'queen_of_hearts')
    QUEEN_OF_SPADES = (10, 'queen_of_spades')
    KING_OF_CLUBS = (10, 'king_of_clubs')
    KING_OF_DIAMONDS = (10, 'king_of_diamonds')
    KING_OF_HEARTS = (10, 'king_of_hearts')
    KING_OF_SPADES = (10, 'king_of_spades')

def deal_card():
    return random.choice(list(PlayingCard))

def calculate_hand(hand):
    value = sum(card.value[0] for card in hand)
    num_aces = sum(1 for card in hand if card in (PlayingCard.ACE_OF_CLUBS, PlayingCard.ACE_OF_DIAMONDS, PlayingCard.ACE_OF_HEARTS, PlayingCard.ACE_OF_SPADES))

    while value <= 11 and num_aces:
        value += 10
        num_aces -= 1

    return value