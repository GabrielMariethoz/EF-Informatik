from random import randint


class Numtrip():
    def __init__(self):
        self.matrix = [
            [4, 4, 32, 16, 64],
            [4, 256, 256, 1024, 1024],
            [8, 32, 512, 2, 4],
            [8, 64, 8, 128, 512],
            [128, 256, 512, 8, 16]
            ]
        self.zeilennummer = 1
        self.instance = "Darstellen"

    def minus(self):
        print("   +------+------+------+------+------+")

    def zahl(self, zahl_m):
        if zahl_m == 2:
            color = "\033[31m"
        elif zahl_m == 4:
            color = "\033[32m"
        elif zahl_m == 8:
            color = "\033[33m"
        elif zahl_m == 16:
            color = "\033[34m"
        elif zahl_m == 32:
            color = "\033[35m"
        elif zahl_m == 64:
            color = "\033[36m"
        elif zahl_m == 128:
            color = "\033[30;1m"
        elif zahl_m == 256:
            color = "\033[31;1m"
        elif zahl_m == 512:
            color = "\033[33;1m"
        elif zahl_m == 1024:
            color = "\033[34;1m"

        if zahl_m < 10:
            return f"|{color}   {zahl_m} \033[0m"
        elif zahl_m < 100:
            return f"|{color}  {zahl_m} \033[0m"
        elif zahl_m < 1000:
            return f"|{color}  {zahl_m}\033[0m"
        else:
            return f"|{color} {zahl_m}\033[0m"

    def zeile(self, zeile):
        zeile_m = []
        for zahl_m in zeile:
            zeile_m.append(self.zahl(zahl_m))
        print(f"{self.zeilennummer} ", zeile_m[0], zeile_m[1], zeile_m[2], zeile_m[3], zeile_m[4], "|")
        self.zeilennummer += 1

    def l_zeile(self):
        print("   |      |      |      |      |      |")

    def spaltennummer(self):
        print("       1      2      3      4      5")

    def darstellen(self, matrix):
        self.spaltennummer()
        self.minus()
        for zeile_m in matrix:
            self.l_zeile()
            self.zeile(zeile_m)
            self.l_zeile()
            self.minus()
        self.zeilennummer = 1
        self.instance = "Input"

    def choose_instance(self):
        if self.instance == "Darstellen":
            self.darstellen(self.matrix)
        elif self.instance == "Input":
            self.eingabe()

    def eingabe(self):
        eingabe_gueltig = False
        while not eingabe_gueltig:
            feld_eingabe = input("Geben Sie ein Feld ein: ")
            if feld_eingabe.isalnum():
                feld_eingabe.replace(" ", "")
                if feld_eingabe.isnumeric() and len(feld_eingabe) == 2:
                    eingabe_gueltig = True

        self.instance = "Darstellen"


numtrip = Numtrip()
while True:
    numtrip.choose_instance()
