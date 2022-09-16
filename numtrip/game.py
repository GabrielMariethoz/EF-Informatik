from random import randint

matrix = [
    [4, 4, 32, 16, 64],
    [4, 256, 256, 1024, 1024],
    [8, 32, 512, 2, 4],
    [8, 64, 8, 128, 512],
    [128, 256, 512, 8, 16]
]


def minus():
    print("+------+------+------+------+------+")


def zahl(zahl_m):
    if zahl_m < 10:
        return f"|   {zahl_m} "
    elif zahl_m < 100:
        return f"|  {zahl_m} "
    elif zahl_m < 1000:
        return f"| {zahl_m} "
    else:
        return f"| {zahl_m}"


def zeile(zeile):
    zeile_m = []
    for zahl_m in zeile:
        zeile_m.append(zahl(zahl_m))
    print(zeile_m[0], zeile_m[1], zeile_m[2], zeile_m[3], zeile_m[4], "|")


def l_zeile():
    print("|      |      |      |      |      |")


def darstellen(matrix):
    minus()
    for zeile_m in matrix:
        l_zeile()
        zeile(zeile_m)
        l_zeile()
        minus()


darstellen(matrix)
