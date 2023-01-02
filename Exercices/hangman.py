import zufallsworte
import sys
# ß ist in den Wörtern

HANGMANS_RAW = ''' 18 Zeichen ergeben ein Bild...
                                         __________        __________        __________        __________        __________        __________        __________        __________        __________
                       |                 |                 |/                |/        |       |/        |       |/        |       |/        |       |/        |       |/        |       |/        |
                       |                 |                 |                 |                 |         O       |         O       |         O       |         O       |         O       |         O
                       |                 |                 |                 |                 |                 |         |       |        -|       |        -|       |        -|-      |        -|-
                       |                 |                 |                 |                 |                 |                 |                 |          \      |          \      |        / \ 
                       |                 |                 |                 |                 |                 |                 |                 |                 |                 |  GAME OVER
    _________         _|_______         _|_______         _|_______         _|_______         _|_______         _|_______         _|_______         _|_______         _|_______         _|_______
___/         \___ ___/         \___ ___/         \___ ___/         \___ ___/         \___ ___/         \___ ___/         \___ ___/         \___ ___/         \___ ___/         \___ ___/         \___
'''.split('\n')[1:-1]  # ohne erste und letzte Zeile


class Hangman():
    def __init__(self):
        self.wort = zufallsworte.zufallswoerter(1)[0]
        while 'ß' in self.wort:
            self.wort = zufallsworte.zufallswoerter(1)[0]

        self.gefunden = []
        self.geraten = []
        self.versuche = 10

    def define_hangman(self):
        self.HANGMAN = []
        for spalte in range(11):
            hangman_spalte = []
            for zeile in HANGMANS_RAW:
                hangman_spalte.append(zeile[(18 * spalte):(18 * (spalte + 1))])
            self.HANGMAN.append("\n".join(hangman_spalte))

    def print_hangman(self, number):
        print(self.HANGMAN[10 - number])

    def wortlaenge(self):
        self.print_hangman(self.versuche)

        for buchstabe in self.wort:
            if buchstabe.lower() in self.gefunden:
                print(buchstabe, end=" ")
            else:
                print("_ ", end=" ")

        print("\n")

    def eingabe(self):

        while True:
            guess = input(f"Geben Sie einen Buchstaben oder ein Wort ein {self.geraten} : ")
            if guess.isalpha():
                return guess
            else:
                print("Diese Eingabe ist nicht gültig. Versuchen Sie es noch einmal. ")

    def test(self):
        self.wortlaenge()

        guess = self.eingabe()
        print("\n")
        self.geraten.append(guess)

        if len(guess) == 1:
            for buchstabe in self.wort:
                if buchstabe.lower() == guess.lower():
                    print("Richtig!")
                    self.gefunden.append(guess.lower())
                    self.gefunden.append(guess.capitalize())
                    return
            self.versuche -= 1
            print("Falsch :(")

        else:
            if guess == self.wort:
                self.gewonnen()

    def gewonnen(self):
        print("\nGlückwunsch, Sie haben gewonnen!")
        self.neue_runde()

    def neue_runde(self):
        neue_runde = input("Noch eine Runde? ")
        if neue_runde.lower() == "ja":
            self.__init__()
            self.spielen()
        elif neue_runde.lower() == "nein":
            sys.exit()
        else:
            neue_runde()

    def spielen(self):
        while self.versuche > 0:
            self.test()
            if set(self.wort) <= set(self.gefunden):
                self.gewonnen()

        self.print_hangman(self.versuche)
        print(f"Schade, Sie haben verloren. Das richtige Wort war {self.wort}.")
        self.neue_runde()


hangman = Hangman()
hangman.define_hangman()
hangman.spielen()

print("\n")
