import zufallsworte
# ß ist in den Wörtern


class Hangman():
    def __init__(self):
        self.wort = zufallsworte.zufallswoerter(1)[0]
        self.gefunden = []
        self.versuche = 10

    def wortlaenge(self):
        for buchstabe in self.wort:
            if buchstabe.lower() in self.gefunden:
                print(buchstabe, end=" ")
            else:
                print("_ ", end=" ")

        print("\n")

    def test(self):
        self.wortlaenge()

        guess = input("Geben Sie einen Buchstaben oder ein Wort ein: ")
        print("\n")

        if len(guess) == 1:
            for buchstabe in self.wort:
                if buchstabe.lower() == guess.lower():
                    print("Richtig!")
                    self.gefunden.append(guess.lower())
                    return
            self.versuche -= 1
            print(f"Falsch, es bleiben {self.versuche} Versuche")

        else:
            if guess == self.wort:
                self.gewonnen()

    def gewonnen(self):
        print("Glückwunsch, Sie haben gewonnen!")
        self.neue_runde()

    def neue_runde(self):
        neue_runde = input("Noch eine Runde? ")
        if neue_runde.lower() == "ja":
            self.__init__()
            self.spielen()
        elif neue_runde.lower() == "nein":
            pass
        else:
            neue_runde()

    def spielen(self):
        while self.versuche > 0:
            self.test()
            if len(set(self.wort)) == len(self.gefunden):
                self.gewonnen()

        print(f"Schade, Sie haben verloren. Das richtige Wort war {self.wort}.")
        self.neue_runde()


hangman = Hangman()
hangman.spielen()

print("\n")
