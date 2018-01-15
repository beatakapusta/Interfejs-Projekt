from flask import Flask
from flask import render_template

from karty import karty
from gra import gra
import random

app = Flask(__name__)

"""
app.py – konfiguracja aplikacji Flaska i połączeń z bazą,
gra.py – klasa opisująca grę,
komputer.py – klasa opisująca komputer,

"""

app.secret_key = 'some_secret'

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/gra')
def gra():
    """Rozpoczęcie gry"""
    game = Gra()
    game.start()
    return render_template('gra.html')

@app.route('/zasady')
def zasady():
    """Zasady"""
    return render_template('zasady.html')

if __name__ == '__main__':
    app.run(debug=True)
