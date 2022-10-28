def zeile_g(breite):
    for counter in range(breite):
        print("*", end="")
    print()


def zeile_w(breite):
    print("*", end="")
    for counter in range(breite - 2):
        print(" ", end="")
    print("*")


def main(groesse):
    breite, hoehe = groesse
    zeile_g(breite)
    for counter in range(hoehe - 2):
        zeile_w(breite)
    zeile_g(breite)


def eingabe():
    breite = input("Wie breit soll ihr Sternchen-Rechteck sein?")
    hoehe = input("Wie hoch soll ihr Sternchen-Rechteck sein?")
    return input_testing(breite, hoehe)


def input_testing(breite, hoehe):
    if breite.isnumeric() and hoehe.isnumeric():
        breite = int(breite)
        hoehe = int(hoehe)
        if breite >= 2 and hoehe >= 2:
            return breite, hoehe
    else:
        print("Die Eingaben sollen Zahlen mehr oder gleichgross wie 2 sein. ")
        return eingabe()


main(eingabe())
