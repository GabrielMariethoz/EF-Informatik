import time

zahlen = []
primzahlen = [2]
max_zahl = 1000000
zeit = time.time()

for counter in range(3, max_zahl + 1):
    primzahl_bool = True
    zahl = 0

    while zahl < len(primzahlen) and primzahl_bool:
        if counter % primzahlen[zahl] == 0:
            primzahl_bool = False
        zahl = zahl + 1

    if primzahl_bool:
        primzahlen.append(counter)


print(primzahlen)
print(time.time() - zeit)
