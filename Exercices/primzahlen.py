zahlen = []
primzahlen = []
primzahl_bool = True

for counter in range(2, 101):
    zahlen.append(counter)


for zahl in zahlen:
    for primzahl in primzahlen:
        if zahl % primzahl == 0:
            primzahl_bool = False

    if primzahl_bool == True:
        primzahlen.append(zahl)
    primzahl_bool = True

print(primzahlen)
