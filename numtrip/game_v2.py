import random
import numpy as np
# import playsound  # Für Bombe, man braucht playsound Version 1.2.2 sonst kommt ein Fehler
import sys
import json  # Um Daten zu speichern

# matrix = [
#         [4, 4, 32, 16, 64],
#         [4, 256, 256, 1024, 1024],
#         [8, 32, 512, 2, 4],
#         [8, 64, 8, 128, 512],
#         [128, 256, 512, 8, 16]
#         ]

dateiname = "daten.json"

# Elemente der Matrix zufällig definieren wenn keine Matrix in der .json Datei ist.

matrix = []
with open(dateiname) as f:
    datensammlung = json.load(f)
    if datensammlung["matrix"] == [[0 for j in range(5)] for i in range(5)]:
        matrix = [[random.choice([2, 4, 8, 16]) for i in range(5)] for j in range(5)]
    else:
        matrix = datensammlung["matrix"]


datensammlung = {}
datensammlung["matrix"] = matrix

with open(dateiname, 'w') as f:
    json.dump(datensammlung, f)


def trennzeile():
    '''Gibt eine Trennzeile aus'''
    print("   +------+------+------+------+------+")


def zahl(zahl_m: int) -> str:
    '''Nimmt eine Zahl m und gibt sie als String in einem gewissen Format zurück.

    zahl_m wird eine Farbe entsprechend der Grösse verliehen und Leerschläge werden ebenfalls der Grösse abhängig gegeben. 

    Parameters
    ----------
    zahl_m: Ist die Rohzahl, welche verändert wird. 

    Returns
    -------
    str
        Die veränderte Zahl in Form eines Strings. 
    '''

    if zahl_m == 0:  # Wenn die Zelle keinen Wert hat, soll auch keine Farbe zugeteilt werden.
        pass
    elif zahl_m == 2:
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
    else:  # Für Zahlen grösser als 1024, z.B. 2048
        color = "\033[37m"

    if zahl_m == 0:
        return "|     "
    elif zahl_m < 10:
        return f"|{color}   {zahl_m} \033[0m"
    elif zahl_m < 100:
        return f"|{color}  {zahl_m} \033[0m"
    elif zahl_m < 1000:
        return f"|{color}  {zahl_m}\033[0m"
    else:
        return f"|{color} {zahl_m}\033[0m"


def zeile(zeile: list, zeilennummer: int) -> int:
    '''Gibt eine Zeile mit Zahlen im Format der Funktion zahl() aus.

    Parameters
    ----------
    zeile: Eine Liste mit 5 Werten, welche ausgegeben werden.
    zeilennummer: Die Nummer der Zeile, welche ausgegeben wird. 

    Returns
    -------
    int
        Das ist die nächste Zeilennummer, damit die nächste Zeile bei der nächsten Iteration ausgegeben werden kann. 
    '''

    zeile_m = [zahl(zahl_m) for zahl_m in zeile]

    try:
        print(f"{zeilennummer} ", zeile_m[0], zeile_m[1], zeile_m[2], zeile_m[3], zeile_m[4], "|")
    except IndexError:
        print("Liste zeile_m ist zu klein in Funktion zeile()")

    return zeilennummer + 1


def l_zeile():
    '''Gibt eine leere Zeile aus'''
    print("   |      |      |      |      |      |")


def spaltennummer():
    '''Gibt die Spaltennummern aus'''
    print("       1      2      3      4      5")


def darstellen():
    '''Gibt eine graphische Ausgabe des Spielfeldes'''
    zeilennummer = 1
    spaltennummer()
    trennzeile()
    for zeilennummer, zeile_m in enumerate(matrix, start=1):
        l_zeile()
        zeilennummer = zeile(zeile_m, zeilennummer)
        l_zeile()
        trennzeile()


def eingabe() -> list:
    '''Liest die Eingabe ein und gibt sie zurück. 

    Die Eingabe ist das Feld, welches gelöscht werden muss. 

    Returns
    -------
    list
        Die Indexe des bei der Eingabe ausgewählten Feldes in der Liste matrix.
    '''

    eingabe_gueltig = False
    while not eingabe_gueltig:  # Solange die Eingabe nicht gültig ist, wird nach der Eingabe gefragt.
        feld_eingabe = input("Geben Sie ein Feld ein: ")
        feld_eingabe = feld_eingabe.replace(" ", "")
        if feld_eingabe.isnumeric() and len(feld_eingabe) == 2:
            eingabe_gueltig = True
        else:
            print("Die Eingabe muss in diesem Format sein: Zahl Zahl ; Beispiel 2 5\n")

    return [int(feld_eingabe[0]) - 1, int(feld_eingabe[1]) - 1]


def nachbarsfelder(feld: list, rekursion: bool = True) -> bool:
    '''Testet, ob die nebenliegendenden Felder den gleichen Wert haben

    Die Funktion testet, ob die Felder nebendran den gleichen Wert haben, wenn ja dann setzt es den Wert des nebenliegenden Feldes auf 0 und ruft die Funktion nachbarsfelder() mit dem nebenliegenden Feld als Parameter auf.

    Parameters
    ----------
    feld: Sind die Indexe des Feldes, welches getestet werden muss
    rekursion: Wenn True, dann wird die Funktion rekursiv wieder aufgerufen, wenn False nicht. Ist True wenn nichts anderes vorgegeben. 

    Return
    ------
    bool
        Gibt True zurück, falls ein Nachbarsfeld gewunden wurde, welches den gleichen Wert hat, wie das eingegebene Feld.

    Warnings
    --------
    Die Funktion wird rekursiv aufgerufen, daher kann STACK OVERFLOW geschehen, wenn sie zuviel Male aufgerufen wird
    '''

    alter_wert = matrix[feld[0]][feld[1]]  # Wert des Feldes einspeichern

    if rekursion:
        matrix[feld[0]][feld[1]] = 0  # Falls rekursiert werden sollte, wird der Wert des Feldes zurückgesetzt.

    gleiches_feld = False

    if feld[0] > 0:
        if matrix[feld[0] - 1][feld[1]] == alter_wert:
            gleiches_feld = True

            if rekursion:
                nachbarsfelder([feld[0] - 1, feld[1]])
    if feld[0] < 4:
        if matrix[feld[0] + 1][feld[1]] == alter_wert:
            gleiches_feld = True

            if rekursion:
                nachbarsfelder([feld[0] + 1, feld[1]])
    if feld[1] > 0:
        if matrix[feld[0]][feld[1] - 1] == alter_wert:
            gleiches_feld = True

            if rekursion:
                nachbarsfelder([feld[0], feld[1] - 1])
    if feld[1] < 4:
        if matrix[feld[0]][feld[1] + 1] == alter_wert:
            gleiches_feld = True

            if rekursion:
                nachbarsfelder([feld[0], feld[1] + 1])

    return gleiches_feld


def auffuellen(zeile: int, spalte: int) -> None:
    '''Füllt leere Felder auf, über welchen ein Wert vorhanden ist.

    Für jedes Feld schaut die Funktion, ob ein Feld oberhalb einen Wert hat, wenn ja wird der Wert in das untere Feld verschoben, um einen Fall der Zahl zu simulieren.

    Parameters
    ----------
    zeile: Der Index der Zeile des Feldes in der Matrix.
    spalte: Der Index der Spalte des Feldes in der Matrix.

    Returns
    -------
    None: Die Funktion wird verlassen, wenn ein Wert gefunden worden ist. 
    '''

    for zeile_oberhalb in range(zeile, -1, -1):
        if not matrix[zeile_oberhalb][spalte] == 0:
            matrix[zeile][spalte] = matrix[zeile_oberhalb][spalte]
            matrix[zeile_oberhalb][spalte] = 0
            return


def spielen():
    '''Ist die immer ausgeführte Hauptfunktion, welche zuständig ist für das Spielen. '''

    darstellen()

    moegliche_zahlen = []
    for i_zeile, zeile in enumerate(matrix):
        for i_zahl, zahl in enumerate(zeile):
            if nachbarsfelder([i_zeile, i_zahl], False):
                moegliche_zahlen.append([i_zeile, i_zahl])

    # Wenn es möglich ist ein Feld zu verdoppeln, d.h moegliche_zahlen nicht leer ist, dann soll das Spiel weitergehen.
    if moegliche_zahlen:

        feld = eingabe()
        while feld not in moegliche_zahlen:
            print("Dieses Feld kann nicht verdoppelt werden, da die Nachbarsfelder nicht den gleichen Wert haben. ")
            feld = eingabe()

        # Der Wert des ausgewählten Feldes wird verdoppelt falls ein Nachbarsfeld den gleichen Wert hat.
        alter_wert = matrix[feld[0]][feld[1]]
        nachbarsfelder(feld)
        matrix[feld[0]][feld[1]] = alter_wert * 2

        if matrix[feld[0]][feld[1]] == 2048:
            print("Bravo! Du hast 2048 erreicht und damit gewonnen :)")
            # playsound.playsound("bombe.mp3")

            datensammlung["matrix"] = matrix
            with open(dateiname, 'w') as f:
                json.dump(datensammlung, f)
            sys.exit()

        for spalte in range(5):
            for zeile in range(4, 0, -1):
                if matrix[zeile][spalte] == 0:
                    auffuellen(zeile, spalte)

        # Felder, welche keinen Wert haben, werden mit einer zufälligen Zahl mit random.choice ↓ gefüllt.
        for i_zeile, zeile in enumerate(matrix):
            for i_spalte, spalte in enumerate(matrix[i_zeile]):
                if zeile[i_spalte] == 0:
                    zeile[i_spalte] = random.choice([2, 2, 2, 4, 4, 4, 8])

        with open(dateiname, 'w') as f:
            datensammlung["matrix"] = matrix
            json.dump(datensammlung, f)

    else:
        print("Sie haben das Spiel leider veloren, es gibt keine Möglichkeiten mehr :(, he gotcha schlecht!!!")
        datensammlung["matrix"] = [[0 for j in range(5)] for i in range(5)]
        with open(dateiname, 'w') as f:
            json.dump(datensammlung, f)
        sys.exit()


while True:
    spielen()
