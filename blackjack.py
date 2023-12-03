#blackjack.py
from cards import calculate_hand


def display_hands(player_hand, python_hand):
    return {
        "player_hand": [card.value[1] for card in player_hand],
        "player_total": calculate_hand(player_hand),
        "python_hand": [card.value[1] for card in python_hand[:1]] + ['?']
        }

def display_final_hands(player_hand, python_hand):
    return {
        "player_final_hand": [card.value[1] for card in player_hand],
        "player_final_total": calculate_hand(player_hand),
        "python_final_hand": [card.value[1] for card in python_hand],
        "python_final_total": calculate_hand(python_hand)
        }
    
def decide_winner(name, player_wins, python_wins, tied_game, player_hand, python_hand):
    player_score = calculate_hand(player_hand)
    python_score = calculate_hand(python_hand)

    if player_score > 21 or (python_score <= 21 and python_score > player_score):
        python_wins += 1
        return f"Dealer wins!\nSorry, {name}...", player_wins, python_wins, tied_game
    elif player_score == python_score:
        tied_game += 1
        return "Tie game", player_wins, python_wins, tied_game
    else:
        player_wins += 1
        return f"{name}, you win!", player_wins, python_wins, tied_game