zahlen = []
primzahlen = []
primzahl_bool = True

for counter in range(2, 101):
    zahlen.append(counter)


for zahl in zahlen:
    if primzahl_bool:
        for primzahl in primzahlen:
            if zahl % primzahl == 0:
                primzahl_bool = False

    if primzahl_bool:
        primzahlen.append(zahl)
    primzahl_bool = True

print(primzahlen)
