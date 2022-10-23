import zufallsworte
import sys
# ß ist in den Wörtern


class Hangman():
    def __init__(self):
        self.wort = zufallsworte.zufallswoerter(1)[0]
        while 'ß' in self.wort:
            self.wort = zufallsworte.zufallswoerter(1)[0]

        self.gefunden = []
        self.geraten = []
        self.versuche = 10

    def define_hangman(self):
        self.versuch10 = '''






            _________
        ___/         \___
        '''

        self.versuch9 = '''

             |
             |
             |
             |
             |
            _|_______
        ___/         \___
        '''

        self.versuch8 = '''
             __________
             |
             |
             |
             |
             |
            _|_______
        ___/         \___
        '''

        self.versuch7 = '''
             __________
             |/
             |
             |
             |
             |
            _|_______
        ___/         \___
        '''

        self.versuch6 = '''
             __________
             |/        |
             |
             |
             |
             |
            _|_______
        ___/         \___
        '''

        self.versuch5 = '''
             __________
             |/        |
             |         O
             |
             |
             |
            _|_______
        ___/         \___
        '''

        self.versuch4 = '''
             __________
             |/        |
             |         O
             |         |
             |
             |
            _|_______
        ___/         \___
        '''

        self.versuch3 = '''
             __________
             |/        |
             |         O
             |        -|
             |
             |
            _|_______
        ___/         \___
        '''

        self.versuch2 = '''
             __________
             |/        |
             |         O
             |        -|
             |          \ 
             |
            _|_______
        ___/         \___
        '''

        self.versuch1 = '''
             __________
             |/        |
             |         O
             |        -|-
             |          \ 
             |
            _|_______
        ___/         \___
        '''

        self.versuch0 = '''
             __________
             |/        |
             |         O
             |        -|-
             |        / \ 
             |  GAME OVER
            _|_______
        ___/         \___
        '''

    def print_hangman(self, number):
        match number:
            case 10:
                print(self.versuch10)
            case 9:
                print(self.versuch9)
            case 8:
                print(self.versuch8)
            case 7:
                print(self.versuch7)
            case 6:
                print(self.versuch6)
            case 5:
                print(self.versuch5)
            case 4:
                print(self.versuch4)
            case 3:
                print(self.versuch3)
            case 2:
                print(self.versuch2)
            case 1:
                print(self.versuch1)
            case 0:
                print(self.versuch0)

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

        print(f"Schade, Sie haben verloren. Das richtige Wort war {self.wort}.")
        self.neue_runde()


hangman = Hangman()
hangman.define_hangman()
hangman.spielen()

print("\n")
