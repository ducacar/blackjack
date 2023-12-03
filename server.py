# server.py
import os
from dotenv import load_dotenv
from flask import Flask, render_template
from routes import index, play_blackjack_view, enter_name, show_result
from waitress import serve
from datetime import timedelta

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

app.config['SESSION_COOKIE_SECURE'] = True
app.config['SESSION_COOKIE_HTTPONLY'] = True

app.permanent_session_lifetime = timedelta(minutes=30) 

@app.route("/")
def home():
    return index()
@app.route("/enter_game", methods=['POST'])
def enter_game():
    return enter_name()
@app.route("/blackjack", methods=['GET', 'POST'])
def blackjack():
    return play_blackjack_view()
@app.route("/result", methods=["GET"])
def result():
    return show_result()

@app.errorhandler(Exception)
def handle_exception(error):
    app.logger.error(f'Unhandled Exception: {error}', exc_info=True)
    return render_template('error.html', error=error), 500

if __name__ == "__main__":
    serve_args = [
        'gunicorn',
        'server:app', 
        '-w', '4',     
        '-b', '0.0.0.0:8000',
    ]
    serve(serve_args)