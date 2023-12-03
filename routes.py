#routes.py
from flask import  render_template, request, session, redirect, url_for
from cards import PlayingCard, deal_card, calculate_hand
from blackjack import display_hands, display_final_hands, decide_winner
import html


def index():
    session.clear()
    return render_template("index.html")

def play_blackjack_view():
    
    name = session.get('name', None)
    player_wins = session.get('player_wins', 0)
    python_wins = session.get('python_wins', 0)
    tied_game = session.get('tied_game', 0)
    game_count = session.get('game_count', 0)

    player_hand = [PlayingCard[c] for c in session.get('player_hand', [])]
    python_hand = [PlayingCard[c] for c in session.get('python_hand', [])]

    game_result = ""

    hands = display_hands(player_hand, python_hand)

    def update_scores():
        nonlocal player_wins
        nonlocal python_wins
        nonlocal tied_game  
        
        result = session.get('game_result')
        if result:
            if 'player' in result:
                player_wins += 1
            elif 'python' in result:
                python_wins += 1
            elif 'tie' in result:
                tied_game += 1

        session['player_wins'] = player_wins
        session['python_wins'] = python_wins
        session['tied_game'] = tied_game
    
    if request.method == 'POST':       
        user_action = request.form.get('user_action', '').lower()

        if user_action == 'play_again':            
            session.pop('player_hand', None)
            session.pop('python_hand', None)
            session.pop('game_result', None)

            player_hand = [deal_card(), deal_card()]
            python_hand = [deal_card(), deal_card()]
            game_count += 1

            update_scores()

            session['player_hand'] = [card.name for card in player_hand]
            session['python_hand'] = [card.name for card in python_hand]
            session['game_count'] = game_count
            session['game_result'] = ""

            return redirect(url_for('blackjack'))
            
        if user_action == 'hit':
            player_hand.append(deal_card())
            hands = display_hands(player_hand, python_hand)

            if calculate_hand(player_hand) > 21:
                hands = display_final_hands(player_hand, python_hand)
                game_result, player_wins, python_wins, tied_game = decide_winner(name, player_wins, python_wins, tied_game, player_hand, python_hand)
                session['game_result'] = game_result
                update_scores()
                session['player_hand'] = [card.name for card in player_hand] 
                return redirect(url_for('result', game_result=game_result, hands=hands, name=name, player_wins=player_wins, python_wins=python_wins, tied_game=tied_game, game_count=game_count))  
            hands = display_hands(player_hand, python_hand)            
        elif user_action == 'stand':
            while calculate_hand(python_hand) < calculate_hand(player_hand):
                python_hand.append(deal_card())
            hands = display_final_hands(player_hand, python_hand)
            game_result, player_wins, python_wins, tied_game = decide_winner(name, player_wins, python_wins, tied_game, player_hand, python_hand)
            session['game_result'] = game_result
            update_scores()
            session['python_hand'] = [card.name for card in python_hand]
            return redirect(url_for('result', game_result=game_result, hands=hands, name=name, player_wins=player_wins, python_wins=python_wins, tied_game=tied_game, game_count=game_count))
    
    session['player_hand'] = [card.name for card in player_hand]  
    session['python_hand'] = [card.name for card in python_hand]  
    session['game_count'] = game_count
    session['player_wins'] = player_wins
    session['python_wins'] = python_wins
    session['tied_game'] = tied_game
    session['game_result'] = game_result

    return render_template("blackjack.html", hands=hands, game_result=game_result, name=name, player_wins=player_wins, python_wins=python_wins, tied_game=tied_game, game_count=game_count)
    
def enter_name():
    name = request.form.get('name', '')
    name = html.escape(name)
    if not name:
        name = "Player"
    session['name'] = name
    return render_template("enter_game.html", name=name)

def show_result():
    name = session.get('name', "Player")
    player_wins = session.get('player_wins', 0)
    python_wins = session.get('python_wins', 0)
    tied_game = session.get('tied_game', 0)
    game_count = session.get('game_count', 0)
    game_result = session.get('game_result', "")
    
    player_hand = [PlayingCard[c] for c in session.get('player_hand', [])]
    python_hand = [PlayingCard[c] for c in session.get('python_hand', [])]
    
    hands = display_final_hands(player_hand, python_hand)
    
    return render_template("result.html", game_result=game_result, hands=hands, name=name, player_wins=player_wins, python_wins=python_wins, tied_game=tied_game, game_count=game_count)