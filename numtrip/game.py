from random import randint


def minus():
    print("+------+------+------+------+------+")


def zahl():
    zahl = 2**randint(1, 6)

    if zahl < 10:
        return f"   {zahl}  "
    elif zahl < 100:
        return f"  {zahl}  "


def zeile():
    print(f"|{zahl()}|{zahl()}|{zahl()}|{zahl()}|{zahl()}|")


def l_zeile():
    print("|      |      |      |      |      |")


def darstellen():
    minus()
    for counter in range(5):
        l_zeile()
        zeile()
        l_zeile()
        minus()


darstellen()
