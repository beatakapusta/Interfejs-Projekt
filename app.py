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

class Gra():
    def __init__(self):
        self.pula_kart = ['as_kier', 'dziesiatka_kier', 'krol_kier', 'dama_kier', 'walet_kier','dziewiatka_kier',
                          'as_karo', 'dziesiatka_karo', 'krol_karo', 'dama_karo', 'walet_karo','dziewiatka_karo',
                          'as_trefl', 'dziesiatka_trefl', 'krol_trefl', 'dama_trefl', 'walet_trefl','dziewiatka_trefl',
                          'as_pik', 'dziesiatka_pik', 'krol_pik', 'dama_pik', 'walet_pik','dziewiatka_pik']
        self.karty = []
        self.reka = {}
        self.stol = {}
        self.aktywny_atut = None
        self.kolejka = 1
        self.wygrana = False
        self.przegrana = False



    def start(self,liczba_graczy):
        '''
        Funkcja rozpoczyna grę
        '''
        self.rozdaj_karty(liczba_graczy)

        if liczba_graczy == 2:
            self.reka[1] = Reka(self.rozdaj_karty(liczba_graczy))
            self.reka[2] = Reka(self.rozdaj_karty(liczba_graczy))
        elif liczba_graczy == 3:
            self.reka[1] = Reka(self.rozdaj_karty(liczba_graczy))
            self.reka[2] = Reka(self.rozdaj_karty(liczba_graczy))
            self.reka[3] = Reka(self.rozdaj_karty(liczba_graczy))

    def rozdaj_karty(self, liczba_graczy):
        # Funkcja losuje karty dla gracza

        if liczba_graczy == 2:
            liczba_kart = 10
        elif liczba_graczy == 3:
            liczba_kart = 7

        karty_na_reke = []

        for i in range(0,24):
            obecna_liczba_kart = len(karty_na_reke)
            a = random.choice(self.pula_kart)
            if a not in karty_na_reke:
                print(a)
                karty_na_reke.append(a)


        return karty_na_reke

#########################################
class Karta():
    '''
    Definiuje kartę
    '''
    def __init__(self, kolor, numer, nazwa):
        self.nazwa = nazwa
        self.kolor = kolor
        self.numer = numer

    def __repr__(self):
        return '%s %s %d' % (self.nazwa, self.kolor, self.numer)


class Ruch():
    def __init__(self):
        self.reka = {}

    def __repr__(self):
        return str(self.reka)

    def dlugosc(self):
        dlugosc = len(self.reka)
        return dlugosc

    def dodaj_karte(self, karta):
        dlugosc = len(self.reka)
        self.reka.update({dlugosc: karta})
        return self.reka

    def wyluz_karte(self, id_karta):
        karta = self.reka.get(int(id_karta))
        self.reka.pop(int(id_karta), None)
        return karta


class Reka():
    def __init__(self, reka):
        self.reka = reka

    def __repr__(self):
        return str(self.reka)

    def dlugosc(self):
        dlugosc = len(self.reka)
        return dlugosc

    def dodaj_karte(self, karta):
        dlugosc = len(self.reka)
        self.reka.update({dlugosc: karta})
        return self.reka

    def put_card(self, id_karty):
        karta = self.reka.get(int(id_karty))
        self.reka.pop(int(id_karty), None)
        return karta
